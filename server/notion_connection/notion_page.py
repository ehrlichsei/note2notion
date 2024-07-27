from .notion_access_info import PageAccessInfo
import requests
import json
import logging

class NotionPage:
    """
    This class provides methods for interacting with Notion pages.
    1. connecting to certain Notion page
    2. get/put/delete certain Notion page
    """

    def __init__(self, access_info: PageAccessInfo):
        self.access_info = access_info
        self._base_url = 'https://api.notion.com/v1'
        self.page_name = self.get_page_name()
        self.headers = {
            'Authorization': f'Bearer {self.access_info.get_key()}',
            'Content-Type': 'application/json',
            'Notion-Version': '2022-06-28',
        }

    def test_connection(self):
        url = f'{self._base_url}/pages/{self.access_info.get_access_id()}'
        response = requests.get(url, headers=self.headers)
        is_connected = response.status_code == 200
        if is_connected:
            logging.info("Connection to page successful.")
        else:
            logging.error(f"Failed to connect to page. Status code: {response.status_code}")
        return is_connected

    def get_page_info(self):
        url = f'{self._base_url}/pages/{self.access_info.get_access_id()}'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            page_info = response.json()
            return page_info
        else:
            logging.error(f"Failed to get page info. Status code: {response.status_code}")
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
        url = f'{self._base_url}/pages/{self.access_info.get_access_id()}'
        payload = {
            "properties": properties
        }
        response = requests.patch(url, headers=self.headers, data=json.dumps(payload))
        is_updated = response.status_code == 200
        return is_updated


    def update_title(self, title):
        properties = {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": title  # replace with your page title
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
                        "content": "lalalala"  # replace with your page title
                    }
                }
            ]
        }
    }

    # page.update_page_property(properties)
    page.update_title("hihihihihihidfdfdfd")