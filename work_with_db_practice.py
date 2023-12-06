from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, declared_attr, Session


class Base:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)


class Pep(Base):
    pep_number = Column(Integer, unique=True)
    name = Column(String(200))
    status = Column(String(20))

    def __repr__(self):
        return f'PEP {self.pep_number} {self.name}'


engine = create_engine('sqlite:///sqlite_train.db', echo=True)
Base.metadata.create_all(engine)
session = Session(engine)

results = session.query(Pep).filter(Pep.status == 'Final').all()
print(results)
