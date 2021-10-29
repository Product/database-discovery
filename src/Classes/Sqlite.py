import os
import sqlite3
import dotenv
from sqlalchemy import create_engine

# load .env file
dotenv.load_dotenv(dotenv.find_dotenv())


class Sqlite:

    def __init__(self, table_schema: str, table_name: str, column_name: str, data_type: str, column_type: str):
        self.table_schema = table_schema
        self.table_name = table_name
        self.column_name = column_name
        self.data_type = data_type
        self.column_type = column_type
        self.has_sensitive = "N"
        self.is_empty_table = "N"
        self.regexp_ip = "N"
        self.regex_phone = "N"
        self.regexp_email = "N"
        self.regex_address = "N"
        self.regex_links = "N"
        self.regex_social_media = "N"
        self.regex_cpf = "N"
        self.regex_credit_card = "N"
        self.regex_name = "N"
        self.executed = "N"

    @staticmethod
    def create_connection():
        sqlite3.connect("../base.db")
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

    @staticmethod
    def create_tables():

        engine = create_engine(os.getenv("SQLITE_PATH") + os.getenv("SQLITE_DATABASE"))

        # table: name
        engine.execute('CREATE TABLE IF NOT EXISTS "names" ('
                       'id integer PRIMARY KEY AUTOINCREMENT,'
                       'name VARCHAR (500) '
                       ');')

        # table: terms
        engine.execute('CREATE TABLE IF NOT EXISTS "terms" ('
                       'id integer PRIMARY KEY AUTOINCREMENT,'
                       'term VARCHAR (500) '
                       ');')

        # table: configs
        engine.execute('CREATE TABLE IF NOT EXISTS "configs" ('
                       'id integer PRIMARY KEY AUTOINCREMENT,'
                       'param VARCHAR (100), '
                       'param_valor VARCHAR (500), '
                       'param_system VARCHAR (500), '
                       'start_date DATE, '
                       'end_date DATE '
                       ');')

        # table: base
        engine.execute('CREATE TABLE IF NOT EXISTS "base" ('
                       'id integer PRIMARY KEY AUTOINCREMENT,'
                       'conceitual_data VARCHAR (500), '
                       'data_classification VARCHAR (500), '
                       'table_schema VARCHAR (500), '
                       'table_name VARCHAR (500), '
                       'column_name VARCHAR (500), '
                       'date_type VARCHAR (500), '
                       'column_type VARCHAR (500), '
                       'sql VARCHAR (500), '
                       'has_sensitive VARCHAR (500), '
                       'is_empty_table VARCHAR (500), '
                       'obs VARCHAR (500), '
                       'classification_source VARCHAR (500), '
                       'regex_ip char(1), '
                       'regex_phone char(1), '
                       'regex_email char(1), '
                       'regex_address char(1), '
                       'regex_links char(1), '
                       'regex_social_media char(1), '
                       'regex_cpf char(1), '
                       'regex_credit_card char(1), '
                       'regex_name char(1), '
                       'date datetime, '
                       'executed char(1) '
                       ');')

    @staticmethod
    def insert_mysql_to_sqlite(self, cursor_sqlite=None, con_sqlite=None):

        # Insert a row of data
        cursor_sqlite.execute(
            "INSERT INTO base (TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME, DATE_TYPE, COLUMN_TYPE, HAS_SENSITIVE, "
            "IS_EMPTY_TABLE, REGEX_PHONE, REGEX_EMAIL, REGEX_ADDRESS, REGEX_LINKS, "
            "REGEX_SOCIAL_MEDIA, REGEX_CPF, REGEX_CREDIT_CARD, REGEX_NAME, EXECUTED, REGEX_IP) VALUES ('" +
            self.table_schema + "','" + self.table_name + "','" + self.column_name + "','" + self.data_type + "','" +
            self.column_type + "', '" + self.has_sensitive + "', '" + self.is_empty_table + "', '" + self.regex_phone +
            "', '" + self.regexp_email + "', '" + self.regex_address + "', '" + self.regex_links + "', '"
            + self.regex_social_media + "', '" + self.regex_cpf + "', '" + self.regex_credit_card +
            "', '" + self.regex_name + "', '" + self.executed + "', '" + self.regexp_ip + "');")

        # Save (commit) the changes
        con_sqlite.commit()

        print("Dados inseridos no SQLite.")
