from flask import Blueprint

from flask_restful import Api

from . import resources

blueprint = Blueprint('messages', __name__)
api = Api(blueprint, prefix='/api')

api.add_resource(resources.MessageList, '/messages')
api.add_resource(resources.Message, '/message/<message_key>')
