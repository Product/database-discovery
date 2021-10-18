from Classes.Sqlite import Sqlite
from Classes.Mysql import MysqlDriver

if __name__ == '__main__':
    MysqlDriver.create_connection()
    Sqlite.create_connection()
