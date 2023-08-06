from flask import Flask
from app import routes
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
login_manager = LoginManager(app)
admin = Admin(app, name='Admin Panel', template_mode='bootstrap3')

from app import routes, models

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Create admin views
class UserAdminView(ModelView):
    column_list = ['username', 'email', 'registration_date', 'is_admin']

admin.add_view(UserAdminView(models.User, db.session))
