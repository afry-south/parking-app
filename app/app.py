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

    send_email(name, email, reg)
    
    return render_template("registered.html", name=name, reg=reg)


def send_email(name, reg):
    username="afryparkingapp@gmail.com"
    password="Parking123."

    sender = "afryparkingapp@gmail.com"
    reciever = "marcus.lissner@afry.com>"
    subject = "Parking"
    text = f"Name: {name}\nReg: {reg}"

    message = f"From: {sender}\nTo: {reciever}\nSubject: {subject}\n\n{text}"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(sender, receiver, message)
    server.quit()


app.run(host="0.0.0.0", port=8080, debug=True) # Den här ska inte ligga här när vi deployar grejerna