from main import db

class Model(object):
    @classmethod
    def update(cls,row_id, **kwargs):
        obj = cls.query.get(row_id)
        print(obj)
        for k, v in kwargs.items():
            setattr(obj, k, v)
        db.session.add(obj)
        db.session.commit()

    @classmethod
    def add_user(cls, **kwargs):
        obj = cls(**kwargs)
        db.session.add(obj)
        db.session.commit()

    @classmethod
    def delete(cls, row_id):
        obj = cls.query.get(row_id)
        db.session.delete(obj)
        db.session.commit()