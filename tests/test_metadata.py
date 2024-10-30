import unittest
from metaline.metadata import get_metadata

class TestDBMetadata(unittest.TestCase):

    def test_mysql_metadata(self):
        connection_string = "mysql+pymysql://user:password@localhost/testdb"
        table_name = "your_table"
        metadata = get_metadata(connection_string, table_name)
        self.assertIsNotNone(metadata)

    # Similar tests can be written for PostgreSQL and MSSQL
