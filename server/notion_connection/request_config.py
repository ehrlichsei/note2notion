from .notion_access_info import AccessInfo, DatabaseAccessInfo, PageAccessInfo
from enum import Enum

class RequestType(Enum):
    DATABASE = "databases"
    PAGE = "pages"
    NOT_DEFINED = 0 

class RequestFormat:
    def __init__(self, access_info: AccessInfo, request_type: RequestType = RequestType.NOT_DEFINED):
        self._base_url = 'https://api.notion.com/v1'
        self._type = request_type
        self.access_info = access_info
        self._requet_url = None
        self._payload = {}
        self._headers = self.set_basic_headers()
    
    def get_headers(self):
        return self._headers
    
    def set_basic_headers(self): 
        headers = {
            'Authorization': f'Bearer {self.access_info.get_key()}',
            'Content-Type': 'application/json',
            'Notion-Version': '2022-06-28',
        }
        return headers

    def add_headers(self, key, value):
        self.headers[key] = value

    def set_payload(self, payload):
        self._payload = payload

    def set_request_url(self):
        self._requet_url = f'{self._base_url}/{self._type.value}/{self.access_info.get_access_id()}'
    
    def get_request_url(self):
        return self._requet_url

class DatabaseRequestFormat(RequestFormat):
    def __init__(self, database_access_info: DatabaseAccessInfo):
        super().__init__(database_access_info, RequestType.DATABASE)


class PageRequestFormat(RequestFormat):
    def __init__(self, page_access_info: PageAccessInfo):
        super().__init__(page_access_info, RequestType.PAGE)
