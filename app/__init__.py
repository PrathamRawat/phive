from flask import Flask, render_template, request, flash, redirect, url_for
import sqlite3
app = Flask(__name__)

def execute(cmd, args):
    #TO-DO: Write fxn to execute the database commands and return any results
    pass

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sign_in")
def sign_in():
    return render_template("signin.html")

@app.route('/verify')
def verify():
    username = request.form('username')
    cmd = 'SELECT password FROM users WHERE username=?'
    password = execute(cmd, (username))
    if password == request.form['password']:
        cmd = 'SELECT id FROM users WHERE username=?'
        session['uid'] = execute(cmd, (username))
        flash('Successfully logged in.', 'success')
        return redirect(url_for('homepage'))
    flash('Incorrect username/password combination!', 'error')
    return redirect(url_for('sign_in'))

@app.route("/sign_up")
def sign_up():
    return render_template("signup.html")

@app.route("/create", methods=['POST'])
def create_account():
    username = request.form('username')
    cmd = 'SELECT password FROM users WHERE username=?'
    if execute(cmd, (username)):
        flash('Username is taken!', 'error')
        return redirect(url_for('sign_up'))
    password = request.form['password']
    if password != request.form['verify']:
        flash('Passwords do not match!', 'error')
        return redirect(url_for('sign_up'))
    cmd = 'INSERT INTO users VALUES (?, ?, ?)'
    execute(cmd, (username, password, []))
    cmd = 'SELECT id FROM users WHERE username=?'
    session['uid'] = execute(cmd, (username))
    flash('Account successfully created.', 'success')
    return redirect(url_for('homepage'))

@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")

@app.route("/add_clothing")
def add_clothing():
    return redirect(url_for('settings'))

if __name__ == "__main__":
    app.debug = True
    app.run()
