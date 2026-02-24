from flask import render_template, redirect, url_for, session, Blueprint, flash, request, current_app
from .forms import LoginForm
from .models import User
from . import db

main = Blueprint("main", __name__)

@main.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.password == form.password.data:
            session['user_id'] = user.id
            session['user_name'] = user.name

            flash("Logged in successfully!", "success")
            if user.role == "Admin":
                return redirect(url_for('main.admin'))

        flash("Invalid email or password", "danger")

    return render_template('login.html', form=form)

@main.route('/admin')
def admin():
    return render_template('admin.html')