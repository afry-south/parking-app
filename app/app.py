import smtplib 
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/registered", methods=["POST"])
def register_car():
    name = request.form["name"]
    reg = request.form["reg"]
    
    # username=""
    # password=""

    # FROM = ""
    # TO = ""
    # SUBJECT = "test"
    # TEXT = f"Name: {name}\nReg: {reg}"

    # MESSAGE = f"From: {FROM}\nTo: {TO}\nSubject: {SUBJECT}\n\n{TEXT}"

    # server = smtplib.SMTP('smtp.gmail.com', 587)
    # server.ehlo()
    # server.starttls()
    # server.login(username,password)
    # server.sendmail(FROM, TO, MESSAGE)
    # server.quit()

    return render_template("registered.html", name=name, reg=reg)

app.run(host="0.0.0.0", port=8080, debug=True) # Den här ska inte ligga här när vi deployar grejerna