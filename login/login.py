from flask import Flask, url_for, render_template
from flask import send_file, request, flash, redirect

import flask_login
from passlib.hash import sha256_crypt
from flask_mail import Mail 

import datetime

from database.tools import*
from database.model import*

app = Flask(__name__)
app.secret_key = "orcaarco"
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
app.config.update(DEBUG=True,#EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',    MAIL_PORT=587,    MAIL_USE_SSL=False,    MAIL_USERNAME = "meuemail@gmail.com",    MAIL_PASSWORD = "minhasenha")
mail = Mail(app)
