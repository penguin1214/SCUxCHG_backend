# -*- coding: utf-8 -*-
from app import app, api
from flask_restful import Resource, Api

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}



