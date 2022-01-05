from main import db

class Model(db.Model):
    __abstract__ = True

    def update(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        db.session.add(self)
        db.session.commit()

    @classmethod
    def add(cls, **kwargs):
        obj = cls(**kwargs)
        db.session.add(obj)
        db.session.commit()

    # @classmethod
    # def delete(cls, id):
    #     user_id = db.session.query(cls).get(id)
    #     db.session.delete(user_id)
    #     db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
