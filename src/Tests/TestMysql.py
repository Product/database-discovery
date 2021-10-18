import pytest
from src.Classes.Mysql import MysqlDriver


class TestMysql:
    mysql = MysqlDriver.create_connection()
