import unittest
from unittest.mock import patch, MagicMock
from server.notion_connection.notion_database import NotionDatabase
from server.notion_connection.notion_access_info import DatabaseAccessInfo, PageAccessInfo
from server.notion_connection.notion_page import NotionPage

class TestNotionDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.database_access_info = DatabaseAccessInfo()
        cls.database_access_info.set_access_info_from_dotenv('SECRET_KEY', 'DATABASE_ID_TEST')
    

    @patch('notion_connection.notion_database.requests.get')
    def test_test_connection(self, mock_get):
        pass


    @patch('notion_connection.notion_database.requests.get')
    def test_get_database_info(self, mock_get):
        pass

    @patch('notion_connection.notion_database.requests.post')
    def test_get_all_pages(self, mock_post):
        pass

if __name__ == '__main__':
    unittest.main()
