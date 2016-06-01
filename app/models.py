# -*- coding: utf-8 -*-
from app import db

class baseEntity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    password = db.Column(db.String(20))
    array = db.Column(db.String(100))

    def __init__(self, entity):

        return


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    password = db.Column(db.String(20))     #是否需要加密保存
    phone = db.Column(db.String(12))
    campus = db.Column(db.Integer)
    avatar = db.Column(db.String(35))
    reg_date = db.Column(db.String(12))
    level = db.Column(db.Integer)
    auth_token = db.Column(db.String(50))

    def __init__(self, user):
        self.id = user['id']
        self.username = user['username']
        self.password = user['password']
        self.phone = user['phone']
        self.campus = user['campus']
        self.avatar = user['avatar']
        self.reg_date = user['reg_date']
        self.level = user['lever']
        self.auth_token = user['token']


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer)
    name = db.Column(db.String(30))
    price = db.Column(db.Float)
    image = db.Column(db.String(35))
    campus = db.Column(db.Integer)
    quality = db.Column(db.Integer)


class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    is_selected = db.Column(db.Boolean)
    is_bought = db.Column(db.Boolean)
    product_id = db.Column(db.Integer)      #foreign key
    bought_price = db.Column(db.Float)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    is_payed = db.Column(db.Boolean)
    create_date = db.Column(db.String(12))
    pay_date = db.Column(db.String(12))
    transaction_id = db.Column(db.String(500))   #length unknown!!
    # cart_item_ids     how to store list object?
    # cart_item_ids = db.Column(db.String(500))    #json-encoded string to store list obj
    # cart_item_ids is stored in TABLE OrderCartItemRel

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    # product_ids
    # product_ids = db.Column(db.String(500))

class OrderCartItemRel(db.Model):

    """
    Relationship of order and cart item ids

    | id | cart_item_id | product_id
    """
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer)
    cart_item_id = db.Column(db.Integer)


# class CategoryProductRel(db.Model):
#
#     """
#     Relationship of category and products
#     """
#     id = db.Column(db.Integer, primary_key=True)
#     category_id = db.Column(db.Integer)
#     product_id = db.Column(db.Integer)


class ImgActivity(db.Model):

    """
    To store image path displayed in HomeTab as current activities.
    """
    id = db.Column(db.Integer, primary_key=True)
    # absolute path: /app/static/img/activity/img_name.jpg  img_path should be: 'activity/img_name.jpg'
    img_path = db.Column(db.String(120))