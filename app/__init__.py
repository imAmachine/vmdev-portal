from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

#login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    db.init_app(app)

    with app.app_context():
        from routes import main_bp
        app.register_blueprint(main_bp)
        db.create_all()
        #login_manager.init_app(app)

    return app
