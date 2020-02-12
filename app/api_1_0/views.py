from flask_restful import Resource, Api
from app.api_1_0 import api_1_0

api_user = Api(api_1_0)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api_user.add_resource(HelloWorld, '/')
