from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://shire_user:fEmGeHCQSlftwWfZpM1Fq29xn0MvxXcL@dpg-cv6a21rtq21c73dh2gjg-a/shire"
app.secret_key="ichascnchdcuncducbeduc"

year= datetime.datetime.now().year

@app.route('/', methods= ["POST", "GET"])
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact', methods= ["POST", "GET"])
def contact():
    return render_template("contact.html")
    
@app.route('/project')
def project():
    return render_template("project.html")


if __name__ == '__main__':
    app.run(debug=True)