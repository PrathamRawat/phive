from flask import Flask, render_template, request, flash, redirect, url_for, session
from utl.matrix import Matrix
from data.data import *
from datetime import date
import sqlite3, urllib3, json
app = Flask(__name__)

app.secret_key = 'temp key'


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
    session['uid'] = addUsers(username, password, Matrix())
    flash('Account successfully created.', 'success')
    return redirect(url_for('settings'))

@app.route("/homepage")
def homepage():
    # TODO: List recommendations if not chosen yet, otherwise list outfit chosen
    outfit = getOutfit(session['uid'], date.today())
    (name, weather, temp, high, low) = get_weather(request.environ['REMOTE_ADDR'])
    if not outfit:
        # TODO: create outfit based on weather
        w = Matrix([
            1 if weather in ['sn', 'sl', 'h'] else 0,
            1 if weather in ['t', 'hr', 'lr', 's'] else 0,
            1 if weather in ['hc', 'lc', 'c'] else 0,
            1 if temp < 40 else 0,
            1 if 40 <= temp < 60 else 0,
            1 if 60 <= temp < 80 else 0,
            1 if 80 <= temp else 0
        ])
        rec = get_recommendations(session['uid'], w).matrix()[0]
        clothes = getAllClothing(session['uid'])
        magnitude = max(rec)
        outfit = []
        while 'bottom' not in [clothing[2] for clothing in outfit] and 'top' not in [clothing[2] for clothing in outfit] and magnitude > 0:
            i = rec.index(magnitude)
            rec.pop(i)
            c = clothes.pop(i)
            if c[2] not in [clothing[2] for clothing in outfit]:
                outfit.append(c)
        session['outfit'] = outfit
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

@app.route("/update_weights", methods=['POST'])
def update_weights():
    (name, weather, temp, high, low) = get_weather(request.environ['REMOTE_ADDR'])
    w = Matrix([
        1 if weather in ['sn', 'sl', 'h'] else 0,
        1 if weather in ['t', 'hr', 'lr', 's'] else 0,
        1 if weather in ['hc', 'lc', 'c'] else 0,
        1 if temp < 40 else 0,
        1 if 40 <= temp < 60 else 0,
        1 if 60 <= temp < 80 else 0,
        1 if 80 <= temp else 0
    ])
    clothing = getAllClothing(session['uid'])
    if request.form['new']:
        weights = getWeight(session['uid'])
        for item in session['outfit']:
            i = clothing.index(item)
            for condition in range(7):
                weights.matrix()[condition][i] = weights.matrix()[condition][i] - w.matrix()[condition] / 3
        return render_template('select.html', clothes=clothing)
    setOutfit(session['uid'], session['outfit'], date.today())
    weights = getWeight(session['uid'])
    for item in session['outfit']:
        i = clothing.index(item)
        for condition in range(7):
            weights.matrix()[condition][i] = weights.matrix()[condition][i] + w.matrix()[condition] / 3
    return redirect(url_for('homepage'))

@app.route("/settings")
def settings():
    clothes = getAllClothing(session['uid'])
    return render_template("settings.html", clothes=clothes)

@app.route("/remove_clothing", methods=['POST'])
def remove_clothing():
    clothing_id = request['id']
    removeClothing(clothing_id)
    return redirect(url_for('settings'))

@app.route("/add_clothing", methods=['POST'])
def add_clothing():
    name = request.form['name']
    picture = request.form['picture']
    ctype = request.form['ctype']
    addClothing(session['uid'], name, ctype, picture)
    matrix = getWeight(session['uid'])
    matrix.add_column([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
    return redirect(url_for('settings'))

if __name__ == "__main__":
    app.debug = True
    app.run()
