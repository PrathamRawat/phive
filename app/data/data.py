import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

DB_FILE = "Drip.db"
db = sqlite3.connect(DB_FILE) #opens existing file or it makes new one if it does not exit
c = db.cursor()               #facilitate db ops


def createUsers():
    command = "CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username TEXT, password TEXT, weights BLOB);"
    c.execute(command)
    return None

def createClothing():
    command = "CREATE TABLE IF NOT EXISTS clothing (clothing_id INTEGER PRIMARY KEY, user_id INTEGER, name TEXT, picture TEXT);"
    c.execute(command)
    return None

def addUsers(username, password, weights):
    """
    adds new user, automatically gives them a unique user_id
    returns user_id
    """
    command = "SELECT user_id FROM users;"
    c.execute(command)
    q = c.fetchall()
    new_id = q[-1][0] + 1
    print(new_id)
    command = "INSERT INTO users VALUES({},\"{}\",\"{}\", {})".format(new_id, username, password, weights)
    c.execute(command)
    print(new_id)
    return(new_id)


def addClothing(user_id, name, picture):
    """
    adds a new clothing item. returns clothing_id
    """
    command = "SELECT clothing_id FROM clothing;"
    c.execute(command)
    q = c.fetchall()
    new_id = q[-1][0] + 1
    print(new_id)
    command = "INSERT INTO clothing VALUES({},{},\"{}\",\"{}\")".format(new_id, user_id, name, picture)
    c.execute(new_id)
    return(new_id)

def getWeight(user_id):
    """
    returns weight given user_id
    """
    command = "SELECT weights FROM users WHERE user_id = " + str(user_id)
    c.execute(command)
    result = c.fetchall()
    weight = result[0][0]
    print(weight)
    return(weight)

def getAllClothing(user_id):
    """
    returns array of (item,link) for each item with user_id
    """
    command = "SELECT name,picture FROM clothing WHERE user_id = {}".format(user_id)
    c.execute(command)
    result = c.fetchall()
    print(result)
    return(result)

def getClothing(user_id, clothing_id):
    """
    returns specific item given user_id and clothing_id
    """
    command = "SELECT name FROM clothing WHERE user_id = {} AND clothing_id = {}".format(user_id, clothing_id)
    c.execute(command)
    result = c.fetchall()
    clothing = result[0][0]
    print(clothing)
    return(clothing)

def changeWeight(user_id, weight):
    """
    changes the weight of user given user_id
    """
    command = "UPDATE users SET weights = \"{}\" WHERE user_id = {};".format(weight, user_id)
    c.execute(command)
    return(weight)

#addUsers('three', 'three', '30.0')
#addUsers(2, 'aaa', 'bbb', '14.0')
#createClothing()
#addClothing(0, 'jacket', 'example.com')
#getWeight(2)
#getClothing(0, 1)
#getAllClothing(0)
#changeWeight(2, 13.0)

db.commit() #save changes
db.close()  #close database
