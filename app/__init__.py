from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sign_in")
def sign_in():
    return render_template("signin.html")

@app.route("/sign_up")
def sign_up():
    return render_template("signup.html")

@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")

if __name__ == "__main__":
    app.debug = True
    app.run()