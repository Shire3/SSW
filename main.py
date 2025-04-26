from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
import datetime


app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='adesolaisa3@gmail.com'
app.config['MAIL_PASSWORD']='gflehshjaavgqdwo'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
app.config['MAIL_DEFAULT_SENDER']='adesolaisa3@gmail.com'

Mail=Mail(app)

year= datetime.datetime.now().year

@app.route('/', methods= ["POST", "GET"])
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/contact", methods= ["GET", "POST"])
def contact():
    if request.method == "POST" :
        message = request.form.get("message")
        user = request.form.get("home")
        user_mail = request.form.get("email")

        msg = Message(
            subject="User feedback",
            recipients= ["adesolaisa3@gmail.com" , "siyishire@gmail.com"],
            body =f"The user {user}, sent a feedback message saying {message} you can respond at {user_mail}",
        )
        Mail.send(msg)
        return "Message sent successfully"
    return render_template("contact.html")

    
@app.route('/project')
def project():
    return render_template("project.html")


if __name__ == '__main__':
    app.run(debug=True)