import mysql.connector

config = {
    'host':'localhost',
    'user':'root',
    'password':'root',
    'database':'MyDatabase',
}

newTable = {"""
            CREATE TABLE items 
            (id INTEGER PRIMARY KEY AUTO_INCREMENT,
            Name VARCHAR (50),
            Price INTEGER (20),)
            """}

def createDb():
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE MyDatabase")
    cursor.close()

def createNewTable():
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE items 
                    (id INTEGER PRIMARY KEY AUTO_INCREMENT,
                    Name VARCHAR (50),
                    Price INTEGER (20)) 
                   ''')
    cursor.close()

def connectDatabase():
    db = mysql.connector.connect(**config)
    return db

def queryDb():
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    cursor.execute("SHOW TABLES")
    
    for x in cursor:
        print(x)

queryDb()