# -*- coding: utf-8 -*-
from app import app, api
from app.api import *

api.add_resource(HelloWorld, '/api/hello')
api.add_resource(Test, '/api/test')
api.add_resource(GetImgArray, '/api/activityImgArray')
api.add_resource(GetImg, '/api/<img_path>')
api.add_resource(GetCategories, '/api/categories')
api.add_resource(GetProductsOfCategory, '/api/category/products', endpoint='products')
api.add_resource(GetProduct, '/api/product', endpoint='product')
api.add_resource(GetAllProductsIdsNamesPairs, '/api/product/all_id_name_pairs')
api.add_resource(SearchProductByName, '/api/product/search_by_name', endpoint='search_by_name')
api.add_resource(LogIn, '/api/user/login')

if __name__ == '__main__':
    app.run(debug=True)

