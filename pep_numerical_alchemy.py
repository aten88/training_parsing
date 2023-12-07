import requests
from bs4 import BeautifulSoup

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, declared_attr, Session

PEP_URL = 'https://peps.python.org/'
response = requests.get(PEP_URL)
soup = BeautifulSoup(response.text, 'lxml')
num_index_section = soup.find(
        'section', attrs={'id': 'numerical-index'}
    )
type_status = [tag.text for tag in num_index_section.find_all('abbr')]

number_title = [number.text for number in num_index_section.find_all(
    'a', attrs={'class': 'pep reference internal'}
)]
numbers = [item for item in number_title if item.isdigit()]

title = [item for item in number_title if not item.isdigit()]

authors = [', '.join(author.stripped_strings) for author in num_index_section.find_all('td')[3::5]]


class PreBase:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)


class Pep(Base):
    type_status = Column(String(2))
    number = Column(Integer, unique=True)
    title = Column(String(200))
    authors = Column(String(200))


engine = create_engine('sqlite:///sqlite.db')

Base.metadata.create_all(engine)
session = Session(engine)

for abbr, numb, name_a, author_name in zip(
    type_status, numbers, title, authors
):
    pep_string = Pep(
        type_status=abbr, number=numb, title=name_a, authors=author_name
    )
    session.add(pep_string)
session.commit()
