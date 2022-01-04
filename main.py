from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from functions import get_dict
from models import *



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False
app.url_map.strict_slashes = False

db = SQLAlchemy(app)


@app.route("/users", methods=["GET", "POST"])
def page_users():
    users = db.session.query(Users).all()
    if request.method == "GET":
        return jsonify(get_dict(users))
    if request.method == "POST":
        data = request.json
        Users.add_user(**data)
        return jsonify(data)

# Get пользователь, PUT - обновление таблицы, Delete удаление записи
@app.route("/users/<int:id>", methods=["GET", "PUT", "DELETE"])
def page_users_id(id):
    user_id = db.session.query(Users).get(id)
    if request.method == "GET":
        return jsonify(get_dict([user_id]))
    if request.method == "PUT":
        data = request.json
        # я решил сделать так, если у кого есть идеи лучше, поделитесь.
        Users.update(id, **data)
        return jsonify(data)
    if request.method == "DELETE":
        Users.delete(id)
        return jsonify(get_dict([user_id]))


@app.route("/orders", methods=["GET", "POST"])
def page_orders():
    orders = db.session.query(Orders).all()
    if request.method == "GET":
        return jsonify(get_dict(orders))
    if request.method == "POST":
        data = request.json
        Orders.add_user(**data)
        return jsonify(data)


@app.route("/orders/<int:id>", methods=["GET", "PUT", "DELETE"])
def page_orders_id(id):
    orders_id = db.session.query(Orders).get(id)
    if request.method == "GET":
        return jsonify(get_dict([orders_id]))
    if request.method == "PUT":
        data = request.json
        # я решил сделать так, если у кого есть идеи лучше, поделитесь.
        Orders.update(id, **data)
        return jsonify(data)
    if request.method == "DELETE":
        Orders.delete(id)
        return jsonify(get_dict([orders_id]))


@app.route("/offers", methods=["GET", "POST"])
def page_offers():
    offers = db.session.query(Offers).all()
    if request.method == "GET":
        return jsonify(get_dict(offers))
    if request.method == "POST":
        data = request.json
        Offers.add_user(**data)
        return jsonify(data)


@app.route("/offers/<int:id>", methods=['get'])
def page_offers_id(id):
    offers_id = db.session.query(Offers).get(id)
    if request.method == "GET":
        return jsonify(get_dict([offers_id]))
    if request.method == "PUT":
        data = request.json
        # я решил сделать так, если у кого есть идеи лучше, поделитесь.
        Offers.update(id, **data)
        return jsonify(data)
    if request.method == "DELETE":
        Offers.delete(id)
        return jsonify(get_dict([offers_id]))


if __name__ == '__main__':
    app.run('127.0.0.1', 8000)
