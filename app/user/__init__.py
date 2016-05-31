from flask import Blueprint

from flask_restful import Api

from . import resources


blueprint = Blueprint('users', __name__)
api = Api(blueprint, prefix='/api')

api.add_resource(resources.UserList, '/users')
api.add_resource(resources.User, '/user/<user_nickname>')
