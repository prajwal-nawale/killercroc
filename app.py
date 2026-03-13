from flask import Flask
from flask_smorest import Api

from db import db
import models
import os

from resources.items import blp as ItemBlueprint
from resources.stores import blp as StoresBlueprint

def create_app():
    app =Flask(__name__)

    app.config["API_TITLE"]="Stores REST API"
    app.config["API_VERSION"]="v1"
    app.config["OPENAPI_VERSION"]="3.0.3"   
    app.config["PROPOGATE_EXCEPTIONS"] =True
    app.config["OPENAPI_URL_PREFIX"]="/"
    app.config["OPENAPI_SWAGGER_UI_PATH"]="/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"]="https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("Database_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
    with app.app_context():
        db.init_app(app)
        db.create_all()

    api=Api(app)
    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoresBlueprint)

    return app

