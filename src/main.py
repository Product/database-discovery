from Classes.Sqlite import Sqlite
from Classes.Mysql import MysqlDriver

if __name__ == '__main__':
    # Create SQLITE tables
    Sqlite.create_tables()

    MysqlDriver.create_connection()
    Sqlite.create_connection()
