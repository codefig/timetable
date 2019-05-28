import MySQLdb as mdb

try:
    db = mdb.connect('127.0.0.1', 'root', '', db='pyqt')
    print("Connected to database")
except mdb.Error as err:
    print("Failed to connect : ", err)