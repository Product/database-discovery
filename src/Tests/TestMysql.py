from src.Classes.Mysql import MysqlDriver
from unittest import TestCase, main


class TestMysql(TestCase):
    def test_connection(self):
        mysql = MysqlDriver.create_connection()
        assert mysql == True

if __name__ == '__main__':
    main()
