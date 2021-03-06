import os

from flask import Flask, request
from flask_restful import Api
from db import db

from resources.goal import Goal

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get( "DATABASE_URL", 'sqlite:///data.db' )
app.secret_key = "MF"
api = Api(app)

api.add_resource( Goal, '/goal/<string:name>' )


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
