import mysql.connector
import os
import dotenv
from mysql.connector import errorcode

# load .env file
dotenv.load_dotenv(dotenv.find_dotenv())


class MysqlDriver:
    def __init__(self, val):
        self.val=val

    @staticmethod
    def create_connection():
        global cnx
        try:
            cnx = mysql.connector.connect(user=os.getenv("MYSQL_USER"), password=os.getenv("MYSQL_PASSWORD"),
                                          host=os.getenv("MYSQL_HOST"),
                                          database=os.getenv("MYSQL_DATABASE"))
            print("Connected to Mysql.")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
                exit()
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
                exit()
            else:
                print(err)
                exit()
        return cnx