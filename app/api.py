# -*- coding: utf-8 -*-

from flask import request
from app import app, api
from flask_restful import Resource, Api

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

class Test(Resource):
    def post(self):
        #printing request.data works
        json_data = request.get_json(force=True)
        print json_data
        return {"result": "success"}
