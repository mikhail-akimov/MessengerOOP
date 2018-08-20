from pytest import raises
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.repository import *
from database.models import Client, ClientContact
from database.base import Base


class TestRepo:
    def setup(self):
        engine = create_engine('sqlite:///:memory:', echo=False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        self.session = session
        c1 = Client('Max')
        session.add(c1)
        c2 = Client('Leo')
        session.add(c2)
        c3 = Client('Kate')
        session.add(c3)

        obj = ClientContact(1, 2)
        session.add(obj)
        obj = ClientContact(1, 3)
        session.add(obj)
        obj = ClientContact(2, 3)
        session.add(obj)

        self.repo = Repository(session)

    def test_get_client_by_username(self):
        leo = self.repo.get_client_by_username('Leo')
        assert leo.name == 'Leo'
        # что будет если клиента нет
        n = self.repo.get_client_by_username('None')
        # вернется None
        assert n is None

    def test_client_exist(self):
        # такой есть
        assert self.repo.client_exists('Leo')
        # такого нету
        assert not self.repo.client_exists('None')

    def test_add_client(self):
        self.repo.add_client('New')
        assert self.repo.client_exists('New')

    def test_get_contacts(self):
        # возьмем контакты Kate
        contacts = self.repo.get_contacts('Kate')
        assert len(contacts) == 0
        # контакты Leo
        contacts = self.repo.get_contacts('Leo')
        assert len(contacts) == 1
        assert contacts[0].name == 'Kate'
        # контакты Max
        contacts = self.repo.get_contacts('Max')
        assert len(contacts) == 2
        # контакты неизвестного человека
        contacts = self.repo.get_contacts('None')
        assert [] == contacts

    def test_add_del_contact(self):
        # создадим нового пользователя
        self.repo.add_client('New')
        # добавим ему контакт
        self.repo.add_contact('New', 'Kate')
        # проверим
        contacts = self.repo.get_contacts('New')
        assert len(contacts) == 1
        assert contacts[0].name == 'Kate'
        # добавим ему контакт которого нет в базе
        # что должно произойти, ошибка или ничего? скорее всего ошибка такого контакта нет в базе
        with raises(ContactDoesNotExist):
            self.repo.add_contact('New', 'None')
        # удалим контакт которого у него нет
        with raises(ContactDoesNotExist):
            self.repo.del_contact('New', 'None')

        # что будет если добавить контакт клиенту которого нет в базе?
        # такое поведение не должно быть возможно впринципе, поэтому проверять пока не будем

    def teardown(self):
        # не забываем удалить тестовые объекты и откатить измененея
        self.session.rollback()
