from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash

from app import db
from app.main.forms import RegisterForm, LoginForm
from app.main.models import User
from app.main.decorators import requires_login

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/')
def home():
    return render_template("main.html")
