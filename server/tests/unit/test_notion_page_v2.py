import unittest
from unittest.mock import patch, Mock
from server.notion_connection.notion_base import NotionPageV2
from server.notion_connection.notion_access_info import PageAccessInfo
from server.notion_connection.request_config import PageRequestFormat

class TestNotionPageV2(unittest.TestCase):

    @patch('notion_connection.notion_base.requests.get')
    def test_get_item_name(self, mock_get):
        # 设置模拟返回值
        mock_response = Mock()
        expected_json = {
            'properties': {
                'Name': {
                    'title': [
                        {'plain_text': 'Test Page'}
                    ]
                }
            }
        }
        mock_response.status_code = 200
        mock_response.json.return_value = expected_json
        mock_get.return_value = mock_response
        
        # 初始化对象
        page_access_info = PageAccessInfo(secret_key="dummy_token", page_id="dummy_page_id")
        page_request_format = PageRequestFormat(page_access_info)
        notion_page = NotionPageV2(page_request_format)
        
        # 测试方法
        item_name = notion_page.get_item_name()
        self.assertEqual(item_name, 'Test Page')

if __name__ == '__main__':
    unittest.main()
