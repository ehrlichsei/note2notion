from dotenv import load_dotenv
import os

load_dotenv()


get_key = lambda x: os.getenv(x)

class AccessInfo:
    def __init__(self, secret_key, access_id):
        self.secret_key = secret_key
        self.access_id = access_id

    def set_access_info_from_dotenv(self, secret_key_key, access_id_key):
        self.secret_key = os.getenv(secret_key_key)
        self.access_id = os.getenv(access_id_key)

    
    def get_key(self):
        return self.secret_key
    
    def get_access_id(self):
        return self.access_id
    
    def print_access_info(self):
        print(self.secret_key)
        print(self.access_id)

class DatabaseAccessInfo(AccessInfo):
    def __init__(self, secret_key = None, database_id = None):
        super().__init__(secret_key, database_id)

class PageAccessInfo(AccessInfo):
    def __init__(self, secret_key = None, page_id = None):
        super().__init__(secret_key, page_id)


class AccessHeaders:
    pass

class PageAccessHeaders(AccessHeaders):
    pass

class DatabaseAccessHeaders(AccessHeaders):
    pass
    


if __name__ == '__main__':
    access_info = DatabaseAccessInfo()
    access_info.set_access_info_from_dotenv("SECRET_KEY", "database_id_inspiration")
    access_info.print_access_info()

    print(get_key("SECRET_KEY"))