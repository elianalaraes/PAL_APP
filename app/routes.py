from flask import render_template, redirect, url_for, session, Blueprint, flash, request, current_app
from .forms import LoginForm
main = Blueprint("main", __name__)

@main.route('/')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)