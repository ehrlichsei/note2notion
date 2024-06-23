from .notion_access_info import AccessInfo, DatabaseAccessInfo, PageAccessInfo
from .request_config import RequestFormat, RequestType, DatabaseRequestFormat, PageRequestFormat
import requests

class NotionBase:

    def __init__(self, request_format: RequestFormat):
        self.request_format = request_format


    def is_connected(self):
        if self._get_item_info():
            return True

    def _get_item_info(self):
        url = self.request_format.get_request_url()
        headers = self.request_format.get_headers()
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            item_info = response.json()
            return item_info
        else:
            print(f"Failed to get item info. Status code: {response.status_code}")
            return None
    
    def get_item_name(self):
        pass

    def update_item_name(self, name):
        pass
    
class NotionPageV2(NotionBase):

    def __init__(self, page_request_format: PageRequestFormat):
        super().__init__(page_request_format)
    def get_item_name(self):
        item_info = self._get_item_info()
        if item_info:
            properties = item_info.get('properties', {})
            name_property = properties.get('Name', {})
            title = name_property.get('title', [])
            plain_texts = [item['plain_text'] for item in title]
            return plain_texts[0]
        else:
            return None
    
    def update_page_property(self, properties):
        payload = {
            "properties": properties
        }
        response = requests.patch(self.request_format.get_request_url(), headers=self.request_format.get_headers(), data=json.dumps(payload))
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
        
class NotionDatabaseV2(NotionBase):

    def __init__(self,  database_request_format: DatabaseRequestFormat):
        super().__init__(database_request_format)
