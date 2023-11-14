from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'main.login'


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    login_manager.init_app(app)
    db.init_app(app)

    with app.app_context():
        from .routes import main_bp
        app.register_blueprint(main_bp)
        db.create_all()

    return app
