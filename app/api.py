# -*- coding: utf-8 -*-

from flask import request, json, url_for, send_file
from app import app, api, db
from flask_restful import Resource, Api, reqparse
from models import *

parser = reqparse.RequestParser()

def responsePacker(result, message, data = "none"):
    return {
        "result": result,
        "message": message,
        "data": data
    }


def requestParser():
    parser.add_argument('data', action='append')
    return  parser.parse_args()['data'][0]


def postDataParser(content):
    return content['data']


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class Test(Resource):
    def post(self):
        print request.headers
        print request.host_url
        # print request.data
        json_data = request.get_json(force=True)
        # print json_data
        # arrstr = json.dumps(json_data['array'])
        # entity = baseEntity(json_data['name'], arrstr)
        # db.session.add(entity)
        # db.session.commit()
        # array = json_data['array']
        # test if password is valid
        # entity = db.session.query(baseEntity).filter(baseEntity.username == json_data['name']).first()
        return {"result": 1,
                "message": "success"}


    def get(self):
        array = db.session.query(baseEntity).filter(baseEntity.id == 1).first().array
        data = json.loads(array)
        return data


class GetImgArray(Resource):
    def get(self):
        # filename = 'static/img/activity/test.jpg'
        # print request.headers
        return {"result": 0,
                "message": "success",
                "data": "[activity/test1]"
                }

class GetImg(Resource):
    def get(self, img_path):
        # parser.add_argument('img_path')
        # arg = parser.parse_args()
        args = img_path.split('+')
        filename = 'static/img/' + args[0] +'/' + args[1] +'.jpg'
        return send_file(filename)

class GetCategories(Resource):
    def get(self):
        raw_categories = db.session.query(Category).all()
        categories = {}
        for category in raw_categories:
            categories[category.id] = category.name
            # print type(category.name)
        if categories:
            return responsePacker(0,"success", categories)

class GetProductsOfCategory(Resource):
    def get(self):
        parser.add_argument('data', action='append')
        category_id = int(parser.parse_args()['data'][0])
        products = db.session.query(Product).filter(Product.category_id == category_id).all()
        product_ids = []
        for product in products:
            product_ids.append(product.id)
        return responsePacker(0, "success", product_ids)

class GetProduct(Resource):
    def get(self):
        data = requestParser()
        print data
        pro_id = int(data)
        product = db.session.query(Product).filter(Product.id == pro_id).first().__dict__
        product.pop('_sa_instance_state')
        return responsePacker(0, "success", product)

class GetAllProductsIdsNamesPairs(Resource):
    def get(self):
        ret = []
        products = db.session.query(Product).all()
        for product in products:
           # ret.append({str(product.id):product.name})
            ret.append(product.name)
        return responsePacker(0, "success", ret)


class SearchProductByName(Resource):
    def get(self):
        ret = []
        parser.add_argument('data', action='append')
        name = '%' + str((parser.parse_args()['data'][0]).encode('utf-8')) +'%'
        # print type(parser.parse_args()['data'][0])
        # print type(name)
        products = db.session.query(Product).filter(Product.name.like(name)).all()
        for product in products:
            ret.append(product.id)
        return responsePacker(0,"success", ret)

class LogIn(Resource):
    def post(self):
        print request.headers
        json_data = request.get_json(force=True)
        print json_data
        data = postDataParser(json_data)
        phone = data['phone']
        password = data['password']
        user = db.session.query(User).filter(User.phone == phone).first()
        print user
        if user:
            ret = user.__dict__
            ret.pop('_sa_instance_state')
            if user.password == password:
                return responsePacker(0, "success", ret)
            else:
                return responsePacker(1, "wrong password")
        else:
            return responsePacker(1, "no user")


