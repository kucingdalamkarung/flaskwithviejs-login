from flask_restful import Resource
from models.models import UserModel, UserSchema, db
from flask_jwt_extended import jwt_required
from flask import request
from libs.utils import Utils


users_schema = UserSchema(many=True, exclude=['password'])
user_schema = UserSchema(exclude=['password'])


class UserResource(Resource):
    @jwt_required
    def get(self, userid=None):
        if userid:
            data = user_schema.dump(UserModel.find_by_id(userid))
            if not data:
                return {'message': 'User not found!'}

            return {'status': 'success', 'user_data': data}
        else:
            data = UserModel.find_all()
            return {'data': data}

    def post(self):
        json_data = request.get_json()
        if not json_data:
            return {'message': 'No data input provided'}

        if user_schema.dump(UserModel.find_by_username(json_data['username'])):
            return {
                'message': 'Username is already exists'
            }

        user = UserModel(
            username=json_data['username'],
            password=Utils.encrypt_pass(json_data['password'])
        )

        user.add()
        res = user_schema.dump(user)

        return {'result': res}

    @jwt_required
    def delete(self, userid):
        return {'user_id': userid}
