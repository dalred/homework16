import json
from models import Users, db, Offers, Orders

def read_json(name):
    data = {}
    with open(name, "r", encoding='utf-8') as file:
        file = file.readline().replace("\'", "\"")
        data = json.loads(file)
    return data

def create_table(path, class_name):
    obj = read_json(path)
    for item in obj:
        user = class_name(**item)
        db.session.add(user)
        db.session.commit()

# def change_roles():
#     for value in db.session.query(Users.role).distinct():
#         usr_roles = Roles(role=value.role)
#         db.session.add(usr_roles)
#         db.session.commit()

def change_users():
    rows = db.session.query(Users.id)
    for k, item in enumerate(rows, 1):
        users = db.session.query(Users).get(k)
        users.id = users.id-1
        db.session.add(users)
        db.session.commit()

if __name__ == '__main__':
    db.create_all()
    create_table('json_files/Users.json', Users)
    create_table('json_files/Offers.json', Offers)
    create_table('json_files/Orders.json', Orders)
    #change_users()