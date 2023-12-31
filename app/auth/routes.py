from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.security import generate_password_hash

from app import login_manager, db
from app.forms import LoginForm, RegistrationForm
from app.models import User, LoginUser

main_bp = Blueprint('main', __name__, static_folder='static', static_url_path='../static', template_folder='templates')


@login_manager.user_loader
def load_user(user_id):
    return LoginUser.get(user_id)


@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route('/registration', methods=['GET', 'POST'])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    if request.method == 'GET':
        regform = RegistrationForm()
        return render_template('register.html', regform=regform)
    elif request.method == 'POST':
        try:
            # Получение данных формы
            login = request.form.get('login')
            password = request.form.get('password')
            name = request.form.get('name')
            surname = request.form.get('surname')
            email = request.form.get('email')

            # Генерация хэша для пароля
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

            new_user = User(login=login, password_hash=hashed_password, email=email,
                            name=name, surname=surname)
            db.session.add(new_user)
            db.session.commit()

            return 'User registered successfully!'
        except Exception:
            return f'Invalid registration'


@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect(url_for('main.index'))
        logform = LoginForm()
        return render_template('login.html', logform=logform)
    elif request.method == 'POST':
        user = User.query.filter_by(login=request.form.get('login')).first()
        password = request.form.get('password')
        if not user:
            return 'Invalid login or password'

        if not user.check_password(password):
            return 'Invalid password'

        login_user(LoginUser(user))
        return redirect('/')


@main_bp.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
