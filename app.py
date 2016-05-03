# -*- coding: utf-8 -*-
from app import app, api
from app.api import HelloWorld, TodoSimple, Test

api.add_resource(HelloWorld, '/')
api.add_resource(TodoSimple, '/<string:todo_id>')
api.add_resource(Test, '/test')

if __name__ == '__main__':
    app.run(debug=True)

