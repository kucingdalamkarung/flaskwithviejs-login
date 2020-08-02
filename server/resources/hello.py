from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

# this class just for testing jwt
class HelloResource(Resource):
    @jwt_required
    def get(self, id=None):
        identity = get_jwt_identity()
        if not id:
            return {'message': 'Hello, world!'}
        
        return {'message': 'Hello, world!', 'id': id}
