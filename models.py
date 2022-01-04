from main import db
from func_models import Model

class Users(Model, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    age = db.Column(db.Integer)
    email = db.Column(db.String(255), db.CheckConstraint('email LIKE "%@%"'), nullable=False, unique=True)
    role = db.Column(db.String)
    phone = db.Column(db.String)





class Offers(Model,db.Model):
    __tablename__ = 'offers'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer)
    executor_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    executor = db.relationship("Users")


class Orders(Model, db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    address = db.Column(db.String)
    price = db.Column(db.Integer)
    executor_id = db.Column(db.Integer, db.ForeignKey('offers.executor_id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    executor = db.relationship("Offers")
    customer = db.relationship("Users")