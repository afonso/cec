from flask_restful import Resource


class UserList(Resource):

    def get(self):
        pass

    def post(self):
        pass


class User(Resource):

    def get(self, user_nickname):
        pass

    def put(self, user_nickname):
        pass

    def delete(self, user_nickname):
        pass
