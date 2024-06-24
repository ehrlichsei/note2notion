import unittest
from unittest.mock import MagicMock
from notion_connection.request_config import RequestFormat, DatabaseRequestFormat, PageRequestFormat, RequestType, AccessInfo, DatabaseAccessInfo, PageAccessInfo

class TestRequestFormat(unittest.TestCase):
    def setUp(self):
        # 创建一个 AccessInfo 的 mock 对象
        self.mock_access_info = MagicMock(spec=AccessInfo)
        self.mock_access_info.get_key.return_value = "mock_key"
        self.mock_access_info.get_access_id.return_value = "mock_id"

        # 创建一个 RequestFormat 的实例
        self.request_format = RequestFormat(self.mock_access_info)

    def test_set_basic_headers(self):
        headers = self.request_format.set_basic_headers()
        expected_headers = {
            'Authorization': 'Bearer mock_key',
            'Content-Type': 'application/json',
            'Notion-Version': '2022-06-28',
        }
        self.assertEqual(headers, expected_headers)

    def test_set_request_url(self):
        self.request_format.set_request_url()
        expected_url = 'https://api.notion.com/v1/0/mock_id'
        self.assertEqual(self.request_format.get_request_url(), expected_url)


class TestDatabaseRequestFormat(unittest.TestCase):
    def setUp(self):
        # 创建一个 DatabaseAccessInfo 的 mock 对象
        self.mock_database_access_info = MagicMock(spec=DatabaseAccessInfo)
        self.mock_database_access_info.get_key.return_value = "mock_key"
        self.mock_database_access_info.get_access_id.return_value = "mock_database_id"

        # 创建一个 DatabaseRequestFormat 的实例
        self.database_request_format = DatabaseRequestFormat(self.mock_database_access_info)

    def test_type(self):
        self.assertEqual(self.database_request_format._type, RequestType.DATABASE)

    def test_set_request_url(self):
        self.database_request_format.set_request_url()
        expected_url = 'https://api.notion.com/v1/databases/mock_database_id'
        self.assertEqual(self.database_request_format.get_request_url(), expected_url)
    


class TestPageRequestFormat(unittest.TestCase):
    def setUp(self):
        # 创建一个 PageAccessInfo 的 mock 对象
        self.mock_page_access_info = MagicMock(spec=PageAccessInfo)
        self.mock_page_access_info.get_key.return_value = "mock_key"
        self.mock_page_access_info.get_access_id.return_value = "mock_page_id"

        # 创建一个 PageRequestFormat 的实例
        self.page_request_format = PageRequestFormat(self.mock_page_access_info)

    def test_type(self):
        self.assertEqual(self.page_request_format._type, RequestType.PAGE)

    def test_set_request_url(self):
        self.page_request_format.set_request_url()
        expected_url = 'https://api.notion.com/v1/pages/mock_page_id'
        self.assertEqual(self.page_request_format.get_request_url(), expected_url)


if __name__ == '__main__':
    unittest.main()

