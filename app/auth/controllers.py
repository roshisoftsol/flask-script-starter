from flask import Blueprint, request, redirect, render_template
from flask_user import current_user, login_required, roles_accepted

auth = Blueprint("auth", __name__, url_prefix="/auth")
