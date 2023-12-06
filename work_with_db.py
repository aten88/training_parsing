from sqlalchemy import (
     Column, Integer, String, create_engine,
     insert, select, update, delete
)
from sqlalchemy.orm import Session, declared_attr, declarative_base


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

    def __repr__(self) -> str:
        return f'PEP {self.pep_number} {self.name}'

    def __str__(self) -> str:
        return f'PEP {self.pep_number} {self.name}'


if __name__ == '__main__':
    engine = create_engine('sqlite:///sqlite.db', echo=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    # Удаление обьекта через execute методом delete через фильтр where
    session.execute(
        delete(Pep).where(Pep.status == 'Active')
    )
    session.commit()  # КОММИТ НЕОБХОДИМ ДЛЯ ВНЕСЕНИЯ ИЗМЕНЕНИЙ В БД

    # Обновление обьекта соответствующего фильтру при помощи
    # метода update и фильтра where
    # session.execute(
    #     update(Pep).where(Pep.pep_number == 1000).values(status='Proposal')
    # )
    # session.commit()

    # Чтение обьекта методом execute с использованием метода select
    # и фильтра where
    # result = session.execute(
    #     select(Pep).where(Pep.status == 'Active')
    # )
    # print(result.all())

    # Добавляется объект методом execute
    # session.execute(
    #     insert(Pep).values(
    #         pep_number='1000',
    #         name='Pep from Future',
    #         status='Proposal'
    #     )
    # )
    # session.commit()

    # Устанавливает статус Active для всех обьектов
    # session.query(Pep).update(
    #     {'status': 'Active'}
    # )
    # session.commit()

    # Меняет статус у отфильтрованного объекта
    # pep8 = session.query(Pep).filter(Pep.pep_number == 8).first()
    # pep8.status = 'Closed'
    # session.commit()

    # Удаляет все обьекты которые подпадают под этот фильтр
    # session.query(Pep).filter(Pep.pep_number > 20).delete()
    # session.commit()

    # Создаются объекты и помещаются в БД
    # pep8 = Pep(
    #     pep_number=8,
    #     name='Style Guide for Python Code',
    #     status='Active'
    # )
    # pep20 = Pep(
    #     pep_number=20,
    #     name='The Zen of Python',
    #     status='Active'
    # )
    # pep216 = Pep(
    #     pep_number=216,
    #     name='Docstring Format',
    #     status='Rejected'
    # )
    # session.add(pep8)
    # session.add(pep20)
    # session.add(pep216)
    # session.commit()

    # Выводятся на печать объекты которые соответствуют заданному фильтру
    # results = session.query(Pep).filter(Pep.status == 'Active').all()
    # print(type(results))
