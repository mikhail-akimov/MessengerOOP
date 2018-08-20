import database.models as models


class ContactDoesNotExist(Exception):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Contact {} does not exist'.format(self.name)


class Repository:

    def __init__(self, session):
        self.session = session

    def add_client(self, username):
        new_item = models.Client(username)
        self.session.add(new_item)
        self.session.commit()

    def client_exists(self, username):
        return self.session.query(models.Client).filter(models.Client.name == username).count() > 0

    def get_client_by_username(self, username):
        return self.session.query(models.Client).filter(models.Client.name == username).first()

    def add_contact(self, client_username, contact_username):
        contact = self.get_client_by_username(contact_username)
        if contact:
            client = self.get_client_by_username(client_username)
            if client:
                cc = models.ClientContact(client_id=client.clientId, contact_id=contact.clientId)
                self.session.add(cc)
                self.session.commit()
        else:
            raise ContactDoesNotExist(contact_username)

    def del_contact(self, client_username, contact_username):
        contact = self.get_client_by_username(contact_username)
        if contact:
            client = self.get_client_by_username(client_username)
            if client:
                cc = self.session.query(models.ClientContact).filter(
                    models.ClientContact.clientId == client.clientId).filter(
                    models.ClientContact.contactId == contact.clientId).first()
                self.session.delete(cc)
        else:
            raise ContactDoesNotExist(contact_username)

    def get_contacts(self, client_username):
        client = self.get_client_by_username(client_username)
        result = []
        if client:
            contacts_clients = self.session.query(models.ClientContact).filter(models.ClientContact.clientId == client.clientId)
            for contact_client in contacts_clients:
                contact = self.session.query(models.Client).filter(models.Client.clientId == contact_client.contactId).first()
                result.append(contact)
        return result
