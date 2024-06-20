# from notion_access_info import DatabaseAccessInfo
# from txt_loader import TxtLoader
# from notion_database import NotionDatabase
# from txt2notion import Txt2Notion

from notion_connection.notion_database import NotionDatabase
from notion_connection.notion_access_info import DatabaseAccessInfo
from notion_connection.txt_loader import TxtLoader
from notion_connection.txt2notion import Txt2Notion

if __name__ == '__main__':
    access_info = DatabaseAccessInfo()
    access_info.set_access_info_from_dotenv("SECRET_KEY", "DATABASE_ID_TEST")
    filepath = "demo.txt"

    text_loader = TxtLoader(filepath)
    text_loader.process_lines()

    notion_database = NotionDatabase(access_info)

    txt2notion = Txt2Notion(notion_database, text_loader)

    txt2notion.write_to_notion(start_line=0, frequency=50)