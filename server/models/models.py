from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from libs.utils import Utils


marshmallow = Marshmallow()
db = SQLAlchemy()


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    join_date = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_all(cls):
        def to_json(x):
            return {
                'username': x.username,
                'date_join': Utils.json_serial(x.join_date)
            }
        return {'users': list(map(lambda x: to_json(x), cls.query.all()))}

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def delete(cls, id):
        try:
            row = db.session.filter_by(id=id).delete()
            db.session.commit()

            return {'status': 'seccess', 'row_deleted': row}
        except:
            return {'status': 'failed to delete data'}


class UserSchema(marshmallow.Schema):
    id = fields.Integer()
    username = fields.String(required=True, error_messages={
                             'required': 'Username cannot be empty'})
    password = fields.String(required=True, error_messages={
                             'required': 'Password cannot be empty'})
    join_date = fields.DateTime()
