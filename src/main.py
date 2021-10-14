import mysql.connector
import sqlite3
import dotenv
import os
from mysql.connector import errorcode

#load .env file
dotenv.load_dotenv(dotenv.find_dotenv())

# connection to mysql
try:
    cnx = mysql.connector.connect(user=os.getenv("MYSQL_USER"), password=os.getenv("MYSQL_PASSWORD"),
                            host=os.getenv("MYSQL_HOST"),
                            database='')
    print("Connected")                            
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

# close mysql connection
cnx.close()