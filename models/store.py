from db import db

class StoreModel(db.Model):
    __tablename__="stores"

    id= db.Column(db.Integer,unique=True,  primary_key=True)
    name=db.Column(db.String, unique=False, nullable=False)
    items=db.relationship('ItemModel',back_populates="store", lazy='dynamic')
    