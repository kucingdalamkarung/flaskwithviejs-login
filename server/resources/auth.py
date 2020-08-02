from models.models import UserSchema, UserModel, db
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required
from flask_restful import Resource
from flask import request
from libs.utils import Utils

users_schema = UserSchema(many=True)
user_schema = UserSchema()


class AuthResource(Resource):
    def get(self):
        return {'message': 'This is auth page'}

    def post(self):
        json_data = request.get_json()
        
        if not json_data:
            return {'message': 'No input data provided'}

        user_data = user_schema.load(json_data)

        if not UserModel.find_by_username(username=user_data['username']):
            return {'message': 'Username is not exists'}

        user_ = user_schema.dump(UserModel.find_by_username(username=user_data['username']))
        
        if Utils.decrypt_pass(user_data['password'], user_['password']):
            access_token = create_access_token(user_['username'])
            refresh_token = create_refresh_token(user_['username'])

            return {
                'message': "Login successful!",
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        else:
            return {
                'message': 'Username or password wrong!'
            }


class Logout(Resource):
    @jwt_required
    def post(self):
        pass
        