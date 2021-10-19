from src.Classes.Sqlite import Sqlite
from unittest import TestCase, main


class TestSqlite(TestCase):
    def test_create_connection(self):
        sqlite = Sqlite.create_connection()
        assert sqlite == True

    def test_check_connection(self):
        self.sqllite = Sqlite.check_connection()
        assert self.sqllite is not None


if __name__ == '__main__':
    main()
