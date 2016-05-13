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
        print type(json_data['array'])
        arrstr = json.dumps(json_data['array'])
        entity = baseEntity(json_data['name'], arrstr)
        db.session.add(entity)
        db.session.commit()
        return {"result": "success"}

    def get(self):
        array = db.session.query(baseEntity).filter(baseEntity.id == 1).first().array
        data = json.loads(array)
        return data
