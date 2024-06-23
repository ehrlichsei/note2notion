import unittest
from unittest.mock import patch, Mock
from server.notion_connection.notion_base import NotionDatabaseV2
from server.notion_connection.notion_access_info import DatabaseAccessInfo
from server.notion_connection.request_config import DatabaseRequestFormat

class TestNotionDatabaseV2(unittest.TestCase):

    @patch('server.notion_connection.notion_base.requests.get')
    def test_is_connected(self, mock_get):
        # 设置模拟返回值
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"dummy": "info"}
        mock_get.return_value = mock_response
        
        # 初始化对象
        database_access_info = DatabaseAccessInfo(secret_key="dummy_token", database_id="dummy_database_id")
        database_request_format = DatabaseRequestFormat(database_access_info)
        notion_database = NotionDatabaseV2(database_request_format)
        
        # 测试方法
        self.assertTrue(notion_database.is_connected())

if __name__ == '__main__':
    unittest.main()
