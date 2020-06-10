from flask import Flask, render_template, request, flash, redirect, url_for, session
from app.utl.matrix import Matrix
from app.data.data import *
import sqlite3, urllib3, json
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sign_in")
def sign_in():
    return render_template("signin.html")

@app.route('/verify')
def verify():
    username = request.form('username')
    # TODO: Check username + password pair
    #if password do match
    session['uid'] = getUser(username)
    flash('Successfully logged in.', 'success') 
    return redirect(url_for('homepage'))
    #if password doesn't match
    flash('Incorrect username/password combination!', 'error')
    return redirect(url_for('sign_in'))

@app.route("/sign_up")
def sign_up():
    return render_template("signup.html")

@app.route("/create", methods=['POST'])
def create_account():
    username = request.form['username']
    # TODO: verify that the username is unique
    password = request.form['username']
    if password != request.form['verify']:
        flash('Passwords do not match.', 'error')
        return redirect(url_for('sign_up'))
    session['uid'] = addUsers(username, password, [])
    flash('Account successfully created.', 'success')
    return redirect(url_for('settings'))

@app.route("/homepage")
def homepage():
    # TODO: List recommendations if not chosen yet, otherwise list outfit chosen
    (name, weather, temp, high, low) = get_weather(request.environ['REMOTE_ADDR'])
    if not outfit:
        # TODO: create outfit based on weather
        print('')
    return render_template("homepage.html", outfit=outfit, temp=(temp,high,low), weather=name)

def get_recommendations(uid, weather):
    weight = getWeight(uid)
    return Matrix.multiply(Matrix([weather]), weight)

def get_weather(ip):
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://ip-api.com/json/%s' % ip)
    data = json.loads(r.data)
    lat = data['lat']
    lon = data['lon']
    r = http.request('GET', 'https://www.metaweather.com/api/location/search/?lattlong=%.2f,%.2f' % (lat, lon))
    woeid = json.loads(r.data)[0]['woeid']
    r = http.request('GET', 'https://www.metaweather.com/api/location/%d' % woeid)
    data = json.loads(r.data)['consolidated_weather']
    return (data['weather_state_name'], data['weather_state_abbr'], data['the_temp'], data['min_temp'], data['max_temp']) 

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
    addClothing(session['uid'], name, picture)
    return redirect(url_for('settings'))

if __name__ == "__main__":
    app.debug = True
    app.run()
