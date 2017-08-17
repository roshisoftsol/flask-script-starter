from flask import Blueprint, request, redirect, render_template
from flask_user import current_user, login_required, roles_accepted

root = Blueprint("root", __name__, url_prefix="/")

# The Home page is accessible to anyone
@root.route('/')
def homepage():
	return render_template('root/root.html')
