import smtplib
from flask import Flask, render_template, request, redirect, url_for

gmail = smtplib.SMTP('smtp.gmail.com', 587)
gmail.ehlo()
gmail.starttls()
username = "afryparkingapp@gmail.com"
password = "Parking123."
gmail.login(username, password)

app = Flask(__name__)


@app.route("/")
def index():
    show_modal = "false"
    if "show_modal" in request.args:
        show_modal = request.args["show_modal"]

    print(show_modal)
    return render_template("index.html", show_modal=show_modal)


@app.route("/registered", methods=["POST"])
def register_car():
    reg = request.form["reg"]
    fname = request.form["fname"]
    lname = request.form["lname"]

    # send_email(reg, fname, lname)

    return redirect(url_for("index", show_modal="true"), code=307)


def send_email(reg, fname, lname):
    sender = "afryparkingapp@gmail.com"
    receiver = "afryparkingapp+1@gmail.com"
    subject = "Parking"
    text = f"Name: {fname} {lname}\nReg: {reg}"

    message = f"From: {sender}\nTo: {receiver}\nSubject: {subject}\n\n{text}"

    gmail.sendmail(sender, receiver, message)


# Den här ska inte ligga här när vi deployar grejerna
app.run(host="0.0.0.0", port=8080, debug=True)
gmail.quit()
