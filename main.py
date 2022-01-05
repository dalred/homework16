from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from functions import get_dict
from models import *



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/test_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False
app.url_map.strict_slashes = False

db = SQLAlchemy(app)


@app.route("/users", methods=["GET", "POST"])
def page_users():
    users = Users.query.all()
    if request.method == "GET":
        return make_response(jsonify(get_dict(users), 200))
    if request.method == "POST":
        data = request.json
        #schema=Users()
        #schema.add(**data)
        Users.add(**data)
        return make_response(jsonify(data), 200)

# Get пользователь, PUT - обновление таблицы, Delete удаление записи
@app.route("/users/<int:id>", methods=["GET", "PUT", "DELETE"])
def page_users_id(id):
    user_id = Users.query.get(id)
    if request.method == "GET":
        return make_response(jsonify(get_dict([user_id]), 200))
    if request.method == "PUT":
        data = request.json
        # я решил сделать так, если у кого есть идеи лучше, поделитесь.
        user_id.update(**data)
        return make_response(jsonify(data), 200)
    if request.method == "DELETE":
        #Users.delete(user_id)
        user_id.delete()
        return make_response(jsonify(get_dict([user_id]), 200))


@app.route("/orders", methods=["GET", "POST"])
def page_orders():
    orders = Orders.query.all()
    if request.method == "GET":
        return make_response(jsonify(get_dict(orders), 200))
    if request.method == "POST":
        data = request.json
        Orders.add(**data)
        return make_response(jsonify(data), 200)


@app.route("/orders/<int:id>", methods=["GET", "PUT", "DELETE"])
def page_orders_id(id):
    orders_id = Orders.query.get(id)
    if request.method == "GET":
        return make_response(jsonify(get_dict([orders_id]), 200))
    if request.method == "PUT":
        data = request.json
        orders_id.update(**data)
        return make_response(jsonify(data), 200)
    if request.method == "DELETE":
        orders_id.delete()
        return make_response(jsonify(get_dict([orders_id]), 200))


@app.route("/offers", methods=["GET", "POST"])
def page_offers():
    offers = Offers.query.all()
    if request.method == "GET":
        return make_response(jsonify(get_dict(offers), 200))
    if request.method == "POST":
        data = request.json
        Offers.add(**data)
        return make_response(jsonify(data), 200)


@app.route("/offers/<int:id>", methods=['get'])
def page_offers_id(id):
    offers_id = Offers.query.get(id)
    if request.method == "GET":
        return make_response(jsonify(get_dict([offers_id]), 200))
    if request.method == "PUT":
        data = request.json
        offers_id.update(**data)
        return make_response(jsonify(data), 200)
    if request.method == "DELETE":
        offers_id.delete()
        return make_response(jsonify(get_dict([offers_id]), 200))


if __name__ == '__main__':
    app.run('127.0.0.1', 8000)
