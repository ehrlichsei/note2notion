import unittest
from server.notion_connection.notion_database import NotionDatabase
from server.notion_connection.notion_access_info import DatabaseAccessInfo, PageAccessInfo
from server.notion_connection.notion_page import NotionPage

class TestNotionAPIConnection(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.database_access_info = DatabaseAccessInfo()
        cls.database_access_info.set_access_info_from_dotenv('SECRET_KEY', 'DATABASE_ID_TEST')
        cls.database_access_info.print_access_info()

        cls.page_access_info = PageAccessInfo()
        cls.page_access_info.set_access_info_from_dotenv('SECRET_KEY', 'PAGE_ID_TEST')

    def test_notion_database_connection(self):
        notion_db = NotionDatabase(self.database_access_info)
        result = notion_db.test_connection()
        self.assertTrue(result)
    
    def test_notion_page_connection(self):
        notion_page = NotionPage(self.page_access_info)
        result = notion_page.test_connection()
        self.assertTrue(result)



if __name__ == '__main__':
    unittest.main()
