import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

DB_FILE = "Drip.db"
db = sqlite3.connect(DB_FILE) #opens existing file or it makes new one if it does not exit
c = db.cursor()               #facilitate db ops


def createUsers():
    DB_FILE = "Drip.db"
    db = sqlite3.connect(DB_FILE) #opens existing file or it makes new one if it does not exit
    c = db.cursor()               #facilitate db ops
    command = "CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username TEXT, password TEXT, weights TEXT, outfit TEXT);"
    c.execute(command)
    db.commit() #save changes
    db.close()  #close database
    return None

def createClothing():
    DB_FILE = "Drip.db"
    db = sqlite3.connect(DB_FILE) #opens existing file or it makes new one if it does not exit
    c = db.cursor()               #facilitate db ops
    command = "CREATE TABLE IF NOT EXISTS clothing (clothing_id INTEGER PRIMARY KEY, user_id INTEGER, name TEXT, type TEXT, picture TEXT);"
    c.execute(command)
    db.commit() #save changes
    db.close()  #close database
    return None

def addUsers(username, password, weights):
    """
    adds new user, automatically gives them a unique user_id
    returns user_id
    """
    DB_FILE = "Drip.db"
    db = sqlite3.connect(DB_FILE) #opens existing file or it makes new one if it does not exit
    c = db.cursor()               #facilitate db ops
    command = "SELECT user_id FROM users;"
    c.execute(command)
    q = c.fetchall()
    new_id = q[-1][0] + 1
    #q[-1][0] + 1
    print(new_id)
    command = "INSERT INTO users VALUES({},\"{}\",\"{}\",\"{}\",\"{}\");".format(new_id, username, password, weights, "outfit")
    c.execute(command)
    db.commit() #save changes
    db.close()  #close database

    print(new_id)
    return(new_id)


def addClothing(user_id, name, ctype, picture):
    """
    adds a new clothing item. returns clothing_id
    """
    DB_FILE = "Drip.db"
    db = sqlite3.connect(DB_FILE) #opens existing file or it makes new one if it does not exit
    c = db.cursor()               #facilitate db ops
    command = "SELECT clothing_id FROM clothing;"
    c.execute(command)
    q = c.fetchall()
    new_id = q[-1][0] + 1
    print(new_id)
    command = "INSERT INTO clothing VALUES({},{},\"{}\",\"{}\",\"{}\")".format(new_id, user_id, name, ctype, picture)
    c.execute(command)
    db.commit() #save changes
    db.close()  #close database
    return(new_id)

def getUser(username):
    """
    checks if username exists
    """
    DB_FILE = "Drip.db"
    db = sqlite3.connect(DB_FILE) #opens existing file or it makes new one if it does not exit
    c = db.cursor()               #facilitate db ops
    command = "SELECT user_id FROM users WHERE username = \"" + username + "\";"
    c.execute(command)
    result = c.fetchall()
    try:
        result[0][0]
        print("valid")
        return result[0][0]
    except:
        print("already taken")
        return False
    db.commit() #save changes
    db.close()  #close database
    return(False)

def getPassword(username):
    """
    returns password given username
    """
    DB_FILE = "Drip.db"
    db = sqlite3.connect(DB_FILE) #opens existing file or it makes new one if it does not exit
    c = db.cursor()               #facilitate db ops
    command = "SELECT password FROM users WHERE username = \"" + username + "\";"
    c.execute(command)
    result = c.fetchall()
    password = result[0][0]
    db.commit() #save changes
    db.close()  #close database
    print(password)
    return(password)

def getWeight(user_id):
    """
    returns weight given user_id
    """
    DB_FILE = "Drip.db"
    db = sqlite3.connect(DB_FILE) #opens existing file or it makes new one if it does not exit
    c = db.cursor()               #facilitate db ops
    command = "SELECT weights FROM users WHERE user_id = " + str(user_id)
    c.execute(command)
    result = c.fetchall()
    if(len(result) == 0):
        return []
    weight = result[0][0]
    db.commit() #save changes
    db.close()  #close database
    print(weight)
    return(weight)

def getAllClothing(user_id):
    """
    returns array of (item,link) for each item with user_id
    """
    DB_FILE = "Drip.db"
    db = sqlite3.connect(DB_FILE) #opens existing file or it makes new one if it does not exit
    c = db.cursor()               #facilitate db ops
    command = "SELECT clothing_id,name,type,picture FROM clothing WHERE user_id = {}".format(user_id)
    c.execute(command)
    result = c.fetchall()
    db.commit() #save changes
    db.close()  #close database
    print(result)
    return(result)

def getClothing(user_id, clothing_id):
    """
    returns specific item given user_id and clothing_id
    """
    DB_FILE = "Drip.db"
    db = sqlite3.connect(DB_FILE) #opens existing file or it makes new one if it does not exit
    c = db.cursor()               #facilitate db ops
    command = "SELECT name FROM clothing WHERE user_id = {} AND clothing_id = {}".format(user_id, clothing_id)
    c.execute(command)
    result = c.fetchall()
    clothing = result[0][0]
    db.commit() #save changes
    db.close()  #close database
    print(clothing)
    return(clothing)

def changeWeight(user_id, weight):
    """
    changes the weight of user given user_id
    """
    DB_FILE = "Drip.db"
    db = sqlite3.connect(DB_FILE) #opens existing file or it makes new one if it does not exit
    c = db.cursor()               #facilitate db ops
    command = "UPDATE users SET weights = \"{}\" WHERE user_id = {};".format(weight, user_id)
    c.execute(command)
    db.commit() #save changes
    db.close()  #close database
    return(weight)

def getOutfit(user_id, date):
    """
    returns the current day's outfit if chosen, else returns an empty list
    """
    DB_FILE = "Drip.db"
    db = sqlite3.connect(DB_FILE) #opens existing file or it makes new one if it does not exit
    c = db.cursor()               #facilitate db ops
    command = "SELECT outfit FROM users WHERE user_id=?;"
    c.execute(command, (user_id,))
    day = c.fetchone()
    db.commit() #save changes
    db.close()  #close database
    if day[0] == date:
        return day[1]
    return []

def setOutfit(user_id, outfit, date):
    """
    returns the current day's outfit if chosen, else returns an empty list
    """
    DB_FILE = "Drip.db"
    db = sqlite3.connect(DB_FILE) #opens existing file or it makes new one if it does not exit
    c = db.cursor()               #facilitate db ops
    command = "UPDATE users SET outfit=? WHERE user_id=?;"
    c.execute(command, [date, ','.join(outfit)], user_id)
    db.commit() #save changes
    db.close()  #close database

#addUsers('two', 'two', 2.0)
#addUsers(2, 'aaa', 'bbb', '14.0')
#createClothing()
#addClothing(0, 'jacket', 'example.com')
#getWeight(0)
#getClothing(0, 1)
#getAllClothing(0)
#changeWeight(2, 13.0)
#createUsers()
#getUser("onedsadas")
#getPassword("one")

db.commit() #save changes
db.close()  #close database
