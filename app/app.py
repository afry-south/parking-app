import smtplib
from flask import Flask, render_template, request

gmail = smtplib.SMTP('smtp.gmail.com', 587)
gmail.ehlo()
gmail.starttls()
username = "afryparkingapp@gmail.com"
password = "Parking123."
gmail.login(username, password)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/registered", methods=["POST"])
def register_car():
    name = request.form["name"]
    reg = request.form["reg"]

    send_email(name, email, reg)

    return render_template("registered.html", name=name, reg=reg)


def send_email(name, reg):
    sender = "afryparkingapp@gmail.com"
    reciever = "marcus.lissner@afry.com>"
    subject = "Parking"
    text = f"Name: {name}\nReg: {reg}"

    message = f"From: {sender}\nTo: {reciever}\nSubject: {subject}\n\n{text}"

    gmail.sendmail(sender, receiver, message)


# Den här ska inte ligga här när vi deployar grejerna
app.run(host="0.0.0.0", port=8080, debug=True)
gmail.quit()
