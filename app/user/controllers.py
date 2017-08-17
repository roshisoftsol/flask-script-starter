from flask import Blueprint, request, redirect, render_template
from flask_user import current_user, login_required, roles_accepted

user = Blueprint("user", __name__, url_prefix="/user")


# The User page is accessible to authenticated users (users that have logged in)
@user.route('/')
@login_required  # Limits access to authenticated users
def user_home():
	return render_template('user/user_home.html')
