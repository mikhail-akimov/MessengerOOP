from database.base import Base, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey


class Client(Base):
    __tablename__ = 'Client'

    clientId = Column(Integer, primary_key=True)

    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Client ('{self.name}')>"

    def __eq__(self, other):
        return self.name == other.name


class ClientContact(Base):
    __tablename__ = "ClientContact"

    clientContactId = Column(Integer, primary_key=True)

    clientId = Column(Integer, ForeignKey('Client.clientId'))
    contactId = Column(Integer, ForeignKey('Client.clientId'))

    def __init__(self, client_id, contact_id):
        self.clientId = client_id
        self.contactId = contact_id


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()
