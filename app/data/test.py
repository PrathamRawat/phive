import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

DB_FILE = "Drip.db"
db = sqlite3.connect(DB_FILE) #opens existing file or it makes new one if it does not exit
c = db.cursor()               #facilitate db ops



command = "CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username TEXT, password TEXT, weights INTEGER);"
c.execute(command)

command = "CREATE TABLE IF NOT EXISTS clothing (clothing_id INTEGER PRIMARY KEY, user_id INTEGER, name TEXT, picture TEXT);"
c.execute(command)
