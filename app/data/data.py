import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

DB_FILE = "Drip.db"
db = sqlite3.connect(DB_FILE) #opens existing file or it makes new one if it does not exit
c = db.cursor()               #facilitate db ops


def createUsers():
    command = "CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username TEXT, password TEXT, weights REAL);"
    c.execute(command)
    return None

def createClothing():
    command = "CREATE TABLE IF NOT EXISTS clothing (clothing_id INTEGER PRIMARY KEY, user_id INTEGER, name TEXT, picture TEXT);"
    c.execute(command)
    return None

def addUsers(username, password, weights):
    command = "SELECT user_id FROM users;"
    c.execute(command)
    q = c.fetchall()
    new_id = q[-1][0] + 1
    print(new_id)
    command = "INSERT INTO users VALUES({},\"{}\",\"{}\", {})".format(new_id, username, password, weights)
    c.execute(command)
    print(command)
    return None


def addClothing(user_id, name, picture):
    command = "SELECT clothing_id FROM clothing;"
    c.execute(command)
    q = c.fetchall()
    new_id = q[-1][0] + 1
    print(new_id)
    command = "INSERT INTO clothing VALUES({},{},\"{}\",\"{}\")".format(new_id, user_id, name, picture)
    c.execute(command)
    return None


#addUsers('three', 'three', '30.0')
#addUsers(2, 'aaa', 'bbb', '14.0')
createClothing()
addClothing(0, 'jacket', 'example.com')

db.commit() #save changes
db.close()  #close database
