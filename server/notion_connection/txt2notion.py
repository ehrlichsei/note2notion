from .notion_database import NotionDatabase
from .notion_access_info import DatabaseAccessInfo
from .txt_loader import TxtLoader
import time
import os
import logging



class Txt2Notion:

    def __init__(self, notion_database: NotionDatabase, txt_loader: TxtLoader ):
        self.txt_loader = txt_loader
        self.notion_database = notion_database

    def txt2property(self, text):
        properties = {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": text
                        }
                    }
                ]
            }
        }
        return properties


    def write_to_notion(self, start_line=0, frequency=30):
        lines = self.txt_loader.get_lines()
        start_time = time.time()
        lines_written = 0
        for index, line in enumerate(lines):
            if index < start_line:
                continue  # skip lines before start_line
            logging.info(f"Processing line {index}: {line}")
            title = line
            property = self.txt2property(title)
            self.notion_database.add_page(property)
            lines_written += 1
            if lines_written >= frequency:
                elapsed_time = time.time() - start_time
                time.sleep(max(1 - elapsed_time, 0))  # restart after 1 second
                start_time = time.time()  # reset start time
                lines_written = 0  # reset lines written
    

if __name__ == '__main__':


    access_info = DatabaseAccessInfo()
    access_info.set_access_info_from_dotenv("SECRET_KEY", "DATABASE_ID_INSPIRATION")
    print(os.getcwd())
    filepath = "input.txt"

    text_loader = TxtLoader(filepath)
    text_loader.process_lines()

    notion_database = NotionDatabase(access_info)
    notion_database.test_connection()

    txt2notion = Txt2Notion(notion_database, text_loader)

    txt2notion.write_to_notion(start_line=0, frequency=50)