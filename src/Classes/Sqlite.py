import os
import sqlite3
import dotenv
# load .env file
dotenv.load_dotenv(dotenv.find_dotenv())

class Sqlite:

    def __init__(self, val):
        self.val = val

    @staticmethod
    def create_connection():
        conn = sqlite3.connect("base.db")
        print("Connect to SQLITE.")
        return True

    @staticmethod
    def check_connection():
        global sqlite_connection
        try:
            sqlite_connection = sqlite3.connect(os.getenv("SQLITE_DATABASE"))
            cursor = sqlite_connection.cursor()
            print("Database Connected")

            sqlite_select_query = "select sqlite_version();"
            cursor.execute(sqlite_select_query)
            record = cursor.fetchall()
            print("SQLite Database Version is: ", record)
            cursor.close()
            return True
        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
            return False
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print("The SQLite connection is closed")
                return False

