import json
import smtplib
from flask import Flask, render_template, request, redirect, url_for

config = json.load(open("app/config.json","r"))
sender = config["sender"]
password = config["password"]
receiver = config["receiver"]

gmail = smtplib.SMTP('smtp.gmail.com', 587)
gmail.ehlo()
gmail.starttls()
gmail.login(sender, password)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/registered", methods=["POST"])
def register_car():
    reg = request.form["reg"]
    fname = request.form["fname"]
    lname = request.form["lname"]

    send_email(reg, fname, lname)

    return render_template("registered.html", reg=reg, fname=fname, lname=lname)


def send_email(reg, fname, lname):
    subject = "Parking"
    text = f"Name: {fname} {lname}\nReg: {reg}"

    message = f"From: {sender}\nTo: {receiver}\nSubject: {subject}\n\n{text}"

    gmail.sendmail(sender, receiver, message)


# Den här ska inte ligga här när vi deployar grejerna
app.run(host="0.0.0.0", port=8080, debug=True)
gmail.quit()
