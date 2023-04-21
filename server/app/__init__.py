from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_identity
)
from datetime import timedelta


db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    CORS(app, origins=['http://localhost:8080'])

    app.config.from_object('config.Config')

    # JWT configs
    app.config['JWT_SECRET_KEY'] = 'wakanda4ever'
    app.config["JWT_BLACKLIST_ENABLED"] = True
    app.config["JWT_BLACKLIST_TOKEN_CHECKS"] = ["access"]
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

    jwt = JWTManager(app)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    from app import routes, models
    app.register_blueprint(routes.api, url_prefix='/api')

    return app
