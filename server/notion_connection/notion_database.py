import requests
import json
import logging

from .notion_access_info import DatabaseAccessInfo, PageAccessInfo
from .notion_page import NotionPage

class NotionDatabase:

    def __init__(self, access_info: DatabaseAccessInfo):
        self.access_info = access_info
        self._base_url = 'https://api.notion.com/v1'
        # self.pages = self._get_all_pages()

    def test_connection(self):
        url = f'{self._base_url}/databases/{self.access_info.get_access_id()}'
        headers = {
            'Authorization': f'Bearer {self.access_info.get_key()}',
            'Content-Type': 'application/json',
            'Notion-Version': '2022-06-28',
        }
        response = requests.get(url, headers=headers)
        is_connected = response.status_code == 200
        if response.status_code == 200:
            logging.info("Connection to database successful.")
        else:
            logging.error(f"Failed to connect to database. Status code: {response.status_code}")
            print(f"Failed to connect to database. Status code: {response.status_code}")
        return is_connected


    def get_database_info(self):
        url = f'{self._base_url}/databases/{self.access_info.get_access_id()}'
        headers = {
            'Authorization': f'Bearer {self.access_info.get_key()}',
            'Content-Type': 'application/json',
            'Notion-Version': '2022-06-28',
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            database_info = response.json()
            return database_info
        else:
            logging.error(f"Failed to get database info. Status code: {response.status_code}")
            return None
        
    def get_database_name(self):
        database_info = self.get_database_info()
        if database_info:
            title_info = database_info.get('title', [])
            plain_texts = [item['plain_text'] for item in title_info]
            return plain_texts
        else:
            return None
        
    def _get_all_pages(self):
        url = f'{self._base_url}/databases/{self.access_info.get_access_id()}/query'
        headers = {
            'Authorization': f'Bearer {self.access_info.get_key()}',
            'Content-Type': 'application/json',
            'Notion-Version': '2022-06-28',
        }

        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data['results']:
                notion_pages = []
                for page in data['results']:
                    page_id = page['id']
                    # print(f"Page ID: {page_id}")
                    access_info = PageAccessInfo(self.access_info.get_key(), page_id)
                    notion_page = NotionPage(access_info)
                    # print(notion_page.get_page_name())
                    notion_pages.append(notion_page)
                return notion_pages
            else:
                logging.warning("Database is empty.")
                return []
        else:
            logging.error(f"Failed to query database. Status code: {response.status_code}")
            return []
    
    def get_all_page_ids(self):
        url = f'{self._base_url}/databases/{self.access_info.get_access_id()}/query'
        headers = {
            'Authorization': f'Bearer {self.access_info.get_key()}',
            'Content-Type': 'application/json',
            'Notion-Version': '2022-06-28',
        }

        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data['results']:
                page_ids = []
                for page in data['results']:
                    id = page['id']
                    # print(f"Page ID: {page_id}")
                    page_ids.append(id)
                return page_ids
            else:
                logging.warning("Database is empty.")
                return []
        else:
            logging.error(f"Failed to query database. Status code: {response.status_code}")
            return []

    def add_page(self, properties):
        url = f'{self._base_url}/pages'
        headers = {
            'Authorization': f'Bearer {self.access_info.get_key()}',
            'Content-Type': 'application/json',
            'Notion-Version': '2022-06-28',
        }
        payload = {
            "parent": {
                "database_id": self.access_info.get_access_id()
            },
            "properties": properties
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            logging.info("Page added successfully.")
        else:
            logging.error(f"Failed to add page. Status code: {response.status_code}")


    def update_latest_page_property(self, new_properties):
        url = f'{self._base_url}/databases/{self.access_info.get_access_id()}/query'
        headers = {
            'Authorization': f'Bearer {self.access_info.get_key()}',
            'Content-Type': 'application/json',
            'Notion-Version': '2022-06-28',
        }

        # 发送查询请求获取数据库中的最近一个页面
        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data['results']:
                latest_page_id = data['results'][0]['id']  # 获取最近一个页面的 ID
                update_url = f'{self._base_url}/pages/{latest_page_id}'
                payload = {
                    "properties": new_properties
                }
                update_response = requests.patch(update_url, headers=headers, data=json.dumps(payload))
                if update_response.status_code == 200:
                    logging.info(f"Latest page {latest_page_id} property updated successfully.")
                else:
                    logging.error(f"Failed to update latest page property. Status code: {update_response.status_code}")
            else:
                logging.warning("Database is empty. No page to update property.")
        else:
            logging.error(f"Failed to query database. Status code: {response.status_code}")

    def update_latest_pages_properties(self, new_properties, num=30):
        url = f'{self._base_url}/databases/{self.access_info.get_access_id()}/query'
        headers = {
            'Authorization': f'Bearer {self.access_info.get_key()}',
            'Content-Type': 'application/json',
            'Notion-Version': '2022-06-28',
        }

        # 发送查询请求获取数据库中的最近 num 个页面
        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data['results']:
                latest_page_ids = [page['id'] for page in data['results'][:num]]  # 获取最近 num 个页面的 ID
                for page_id in latest_page_ids:
                    update_url = f'{self._base_url}/pages/{page_id}'
                    payload = {
                        "properties": new_properties
                    }
                    update_response = requests.patch(update_url, headers=headers, data=json.dumps(payload))
                    if update_response.status_code == 200:
                        logging.info(f"Page {page_id} property updated successfully.")
                    else:
                        logging.error(f"Failed to update page {page_id} property. Status code: {update_response.status_code}")
            else:
                logging.warning("Database is empty. No page to update property.")
        else:
            logging.error(f"Failed to query database. Status code: {response.status_code}")



if __name__ == '__main__':
    
    access_info = DatabaseAccessInfo()
    access_info.set_access_info_from_dotenv("SECRET_KEY", "DATABASE_ID_TEST")
    access_info.print_access_info()
    notion_db = NotionDatabase(access_info)

    notion_db.test_connection()

    db_name = notion_db.get_database_name()
    if db_name:
        print("Database name:")
        print(db_name)

    # 定义页面属性
    page_properties = {
        "Name": {
            "title": [
                {
                    "text": {
                        "content": "示例页面dfdfdfd"
                    }
                }
            ]
        }
    }

    # 添加页面
    notion_db.add_page(page_properties)

    # 获取所有页面 打印页面名称
    for page in notion_db.pages:
        print(page.page_name)
