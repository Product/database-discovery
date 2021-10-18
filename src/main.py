from Classes.SQLITE import Sqlite
from Classes.MYSQL import MysqlDriver

if __name__ == '__main__':
    MysqlDriver.create_connection()
    Sqlite.create_connection()
