from flask import Flask, render_template, request, flash, redirect, url_for, session
import sqlite3
app = Flask(__name__)

def execute(cmd, args):
    #TODO: Write fxn to execute the database commands and return any results
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
    # TODO: Add default clothing to newly created accounts
    return redirect(url_for('settings'))

@app.route("/homepage")
def homepage():
    # TODO: List recommendations if not chosen yet, otherwise list outfit chosen
    # TODO: Also list the weather for the day
    return render_template("homepage.html")

def get_recommendations():
    recommendations = list()
    # TODO: Use weights to come up with a number of recommendations listed in order of most to least strong
    return recommendations

@app.route("/update_weights")
def update_weights():
#     TODO: Get some form data or somethign to indicate which of the recommendations was chosen
#     TODO: Strengthen the weights between the clothes that were chosen together, and weaken the weights between the ones that weren't
    return redirect(url_for('homepage'))

@app.route("/settings")
def settings():
    # TODO: Display all articles of clothing
    # - Allow for users to remove clothing, and change each of its settings
    return render_template("settings.html")

@app.route("/add_clothing")
def add_clothing():
    name = request.form['name']
    picture = request.form['picture']
    cmd = 'INSERT INTO clothing VALUES (?, ?, ?)'
    execute(cmd, (session['uid'], name, picture))
    return redirect(url_for('settings'))

if __name__ == "__main__":
    app.debug = True
    app.run()
