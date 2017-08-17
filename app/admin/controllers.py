from flask import Blueprint, request, redirect, render_template
from flask_user import current_user, login_required, roles_accepted

admin = Blueprint("admin", __name__, url_prefix="/admin")

# The Admin page is accessible to users with the 'admin' role
@admin.route('/')
@roles_accepted('admin')  # Limits access to users with the 'admin' role
def admin_home():
	return render_template('admin/admin_home.html')