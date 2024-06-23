import unittest
from unittest.mock import patch, MagicMock
from server.notion_connection.notion_access_info import PageAccessInfo  # 假设你的 PageAccessInfo 类来自同一个模块
from server.notion_connection.notion_page import NotionPage  # 假设你的 NotionPage 类来自同一个模块

class TestNotionPage(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # 在整个测试类开始前设置，可以进行一些初始化工作
        cls.access_info = PageAccessInfo()
        cls.access_info.set_access_info_from_dotenv('SECRET_KEY', 'PAGE_ID_TEST')
    
    def setUp(self):
        # 每个测试方法前的准备工作，例如创建一个 NotionPage 实例
        self.page = NotionPage(self.access_info)

    def test_test_connection_success(self):
        # 模拟请求成功的情况
        with patch('requests.get') as mock_get:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_get.return_value = mock_response
            result = self.page.test_connection()
            self.assertTrue(result)

    def test_test_connection_failure(self):
        # 模拟请求失败的情况
        with patch('requests.get') as mock_get:
            mock_response = MagicMock()
            mock_response.status_code = 404  # 模拟请求失败的状态码
            mock_get.return_value = mock_response
            result = self.page.test_connection()
            self.assertFalse(result)  # 由于 test_connection() 方法返回 None，因此这里使用 assertIsNone 断言

    def test_get_page_name(self):
        # 模拟获取页面名称的测试
        expected_page_name = 'Test Page Name'
        mock_page_info = {
            'properties': {
                'Name': {
                    'title': [{'plain_text': expected_page_name}]
                }
            }
        }
        with patch.object(self.page, 'get_page_info', return_value=mock_page_info):
            result = self.page.get_page_name()
            self.assertEqual(result, expected_page_name)
    
    def test_test_api_connected(self):
        result = self.page.test_connection()
        self.assertTrue(result)

    def test_update_page_connected(self):
        new_page_name = 'lalalala'
        properties = {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": new_page_name  # 替换为你的页面标题内容
                        }
                    }
                ]
            }
        }
        result = self.page.update_page_property(properties)
        self.assertTrue (result)

    # 可以继续添加其他的测试方法，覆盖你的其他功能需求

    def tearDown(self):
        # 每个测试方法后的清理工作，例如释放资源
        pass

    @classmethod
    def tearDownClass(cls):
        # 在整个测试类结束后的清理工作
        pass

if __name__ == '__main__':
    unittest.main()

