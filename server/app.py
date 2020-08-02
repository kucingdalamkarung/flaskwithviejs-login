from flask import Blueprint, Flask
from flask_restful import Api
from models.models import db
import config.config as config
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# import resource here
from resources.hello import HelloResource
from resources.user import UserResource
from resources.auth import AuthResource


app = Flask(__name__)
api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)
JWTManager(app)
CORS(app)

# app config here
app.config['JWT_SECRET_KEY'] = 'super_secret'
# uncomment script bellow if you are running without debug mode
# app.config['PROPAGATE_EXCEPTIONS'] = True

app.config.from_object(config)

# register api here
api.add_resource(HelloResource, '/hello', '/hello/<id>')
api.add_resource(UserResource, '/user', '/user/<userid>')
api.add_resource(AuthResource, '/auth')

# register blueprint here
app.register_blueprint(api_blueprint, url_prefix='/api')

# register models here
db.init_app(app)


@app.route('/')
def home():
    return "Hello world"


if __name__ == "__main__":
    app.run()
