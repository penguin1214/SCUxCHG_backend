# -*- coding: utf-8 -*-
from app import app, api
from app.api import HelloWorld, TodoSimple

api.add_resource(HelloWorld, '/')
api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)

