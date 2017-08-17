# This file defines command line commands for manage.py
#
# Copyright 2014 SolidBuilds.com. All rights reserved
#
# Authors: Ling Thio <ling.thio@gmail.com>

import datetime

from app import app, db, manager
from app.auth.models import User, Role


@manager.command
def first_time_setup():
    print('First time setup wizard')
    os.system("python manage.py db upgrade")
    init_db()


@manager.command
def update_project():
    print('Update project wizard')
    os.system("python manage.py db upgrade")


def init_db():
    """ Create users when app starts """
    
    # Adding roles
    admin_role = find_or_create_role('admin', u'Admin')
    user_role = find_or_create_role('user', u'User')

    # Add users
    user = find_or_create_user(u'Admin', u'Example', u'admin@example.com', 'password1', admin_role)
    user = find_or_create_user(u'User', u'Example', u'user@example.com', 'password1', user_role)

    # Save to DB
    db.session.commit()


def find_or_create_role(name, label):
    """ Find existing role or create new role """
    role = Role.query.filter(Role.name == name).first()
    if not role:
        role = Role(name=name, label=label)
        db.session.add(role)
    return role


def find_or_create_user(first_name, last_name, email, password, role=None):
    """ Find existing user or create new user """
    user = User.query.filter(User.email == email).first()
    if not user:
        user = User(email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=app.user_manager.hash_password(password),
                    active=True,
                    confirmed_at=datetime.datetime.utcnow())
        if role:
            user.roles.append(role)
        db.session.add(user)
    return user

