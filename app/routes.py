from flask import Blueprint, render_template

from app.models import *

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route('/users')
def get_users():
    print('hui')
    users = Users.query.all()
    return render_template('users.html', users=users)
