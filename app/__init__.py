from datetime import datetime
from flask import Flask
from flask_mail import Mail
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserManager, SQLAlchemyAdapter
from flask_wtf.csrf import CSRFProtect

# The WSGI compliant web application object
app = Flask(__name__)
app.config.from_object('app.settings')

# Blueprints
from app.auth.controllers import auth
app.register_blueprint(auth)
from app.root.controllers import root
app.register_blueprint(root)
from app.admin.controllers import admin
app.register_blueprint(admin)
from app.user.controllers import user
app.register_blueprint(user)

# Setup Flask-SQLAlchemy
db = SQLAlchemy(app)

# Setup Flask-Script
manager = Manager(app)

# Setup Flask-Migrate
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

# Setup Flask-Mail
mail = Mail(app)

# Setup WTForms CsrfProtect
CSRFProtect(app)

# Define bootstrap_is_hidden_field for flask-bootstrap's bootstrap_wtf.html
from wtforms.fields import HiddenField

def is_hidden_field_filter(field):
    return isinstance(field, HiddenField)

app.jinja_env.globals['bootstrap_is_hidden_field'] = is_hidden_field_filter

# Setup Flask-User to handle user account related forms
from app.auth.models import User, MyRegisterForm

db_adapter = SQLAlchemyAdapter(db, User)  # Setup the SQLAlchemy DB Adapter
user_manager = UserManager(db_adapter, app, register_form=MyRegisterForm)

import app.manage_commands