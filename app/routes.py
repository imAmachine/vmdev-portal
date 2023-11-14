from flask import Blueprint, render_template
from .models import Users

main_bp = Blueprint('main', __name__, static_folder='static', template_folder='templates')


@main_bp.route('/')
def index():
    users = Users.query.all()
    return render_template('index.html', users=users)
