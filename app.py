# -*- coding: utf-8 -*-
from app import app, api
from app.api import HelloWorld

api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run(debug=True)

