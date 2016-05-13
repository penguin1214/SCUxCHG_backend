# -*- coding: utf-8 -*-

from flask import request, json
from app import app, api, db
from flask_restful import Resource, Api
from models import *

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class Test(Resource):
    def post(self):
        #printing request.data works
        json_data = request.get_json(force=True)
        print json_data
        entity = baseEntity(json_data['name'])
        db.session.add(entity)
        db.session.commit()
        return {"result": "success"}
