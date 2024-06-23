from .notion_access_info import PageAccessInfo
import requests
import json

class NotionPage:

    def __init__(self, access_info: PageAccessInfo):
        self._secret_key = access_info.get_key()
        self._page_id = access_info.get_access_id()
        self._base_url = 'https://api.notion.com/v1'
        self.page_name = self.get_page_name()

    def test_connection(self):
        url = f'{self._base_url}/pages/{self._page_id}'
        headers = {
            'Authorization': f'Bearer {self._secret_key}',
            'Content-Type': 'application/json',
            'Notion-Version': '2022-06-28',
        }
        response = requests.get(url, headers=headers)
        is_connected = response.status_code == 200
        return is_connected

    def get_page_info(self):
        url = f'{self._base_url}/pages/{self._page_id}'
        headers = {
            'Authorization': f'Bearer {self._secret_key}',
            'Content-Type': 'application/json',
            'Notion-Version': '2022-06-28',  # 替换为正确的 Notion API 版本
        
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            page_info = response.json()
            return page_info
        else:
            print(f"Failed to get page info. Status code: {response.status_code}")
            return None
        
    def get_page_name(self):
        page_info = self.get_page_info()
        if page_info:
            properties = page_info.get('properties', {})
            name_property = properties.get('Name', {})
            title = name_property.get('title', [])
            plain_texts = [item['plain_text'] for item in title]
            return plain_texts[0]
        else:
            return None
        
    def update_page_property(self, properties):
        url = f'{self._base_url}/pages/{self._page_id}'
        headers = {
            'Authorization': f'Bearer {self._secret_key}',
            'Content-Type': 'application/json',
            'Notion-Version': '2022-06-28',
        }
        payload = {
            "properties": properties
        }
        response = requests.patch(url, headers=headers, data=json.dumps(payload))
        is_updated = response.status_code == 200
        return is_updated


    def update_title(self, title):
        properties = {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": title  # 替换为你的页面标题内容
                        }
                    }
                ]
            }
        }
        self.update_page_property(properties)

        

if __name__ == '__main__':

    access_info = PageAccessInfo()
    access_info.set_access_info_from_dotenv('SECRET_KEY', 'PAGE_ID_TEST')
    page = NotionPage(access_info)
    page.test_connection()
    print(page.get_page_name())

    properties = {
        "Name": {
            "title": [
                {
                    "text": {
                        "content": "lalalala"  # 替换为你的页面标题内容
                    }
                }
            ]
        }
    }

    # page.update_page_property(properties)
    page.update_title("hihihihihihidfdfdfd")