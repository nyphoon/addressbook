from flask_sqlalchemy import SQLAlchemy


def setup_model(db: SQLAlchemy):
    # TODO: how to type hint for return value as AddrBookModel
    #       since it needs to be defined later

    class AddrBook(db.Model):
        _id = db.Column('_id', db.Integer, primary_key=True)
        name = db.Column(db.String(50))
        email = db.Column(db.String(50))
        phone = db.Column(db.String(50))
        address = db.Column(db.String(200))

        def __init__(self, name, email, phone, address):
            self.name = name
            self.email = email
            self.phone = phone
            self.address = address

        def to_dict(self):
            return {'_id': self._id,
                    'name': self.name,
                    'email': self.email,
                    'phone': self.phone,
                    'address': self.address}

    class AddrBookModel:
        def list_all(self):
            return [c.to_dict() for c in AddrBook.query.all()]

        def get(self, addrbook_id):
            addrbook = AddrBook.query.filter_by(_id=addrbook_id).one()
            return None if addrbook is None else addrbook.to_dict()

        def add(self, name, email, phone, address):
            addrbook = AddrBook(name, email, phone, address)
            db.session.add(addrbook)
            db.session.commit()
            db.session.flush()
            db.session.refresh(addrbook)  # get id
            return addrbook._id

        def modify(self, addrbook_id,
                   name = None, email=None, phone=None, address=None):
            addrbook = AddrBook.query.filter_by(_id=addrbook_id).one()
            if name:
                addrbook.name = name
            if email:
                addrbook.email = email
            if phone:
                addrbook.phone = phone
            if address:
                addrbook.address = address
            db.session.commit()
            db.session.flush()
            db.session.refresh(addrbook)  # get id
            return addrbook._id

        def delete(self, addrbook_id):
            addrbook = AddrBook.query.filter_by(_id=addrbook_id).first()
            db.session.delete(addrbook)
            db.session.commit()

    return AddrBookModel()
