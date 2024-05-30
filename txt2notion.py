from notion_database import NotionDatabase
from notion_access_info import DatabaseAccessInfo
from txt_loader import TxtLoader
import time



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
                continue  # 跳过指定行之前的行
            print(f"Processing line {index}: {line}")
            title = line
            property = self.txt2property(title)
            self.notion_database.add_page(property)
            lines_written += 1
            if lines_written >= frequency:
                elapsed_time = time.time() - start_time
                time.sleep(max(1 - elapsed_time, 0))  # 等待剩余时间
                start_time = time.time()  # 重置开始时间
                lines_written = 0  # 重置计数器
    

if __name__ == '__main__':
    access_info = DatabaseAccessInfo()
    access_info.set_access_info_from_dotenv("SECRET_KEY", "DATABASE_ID_TEST")
    filepath = "demo.txt"

    text_loader = TxtLoader(filepath)
    text_loader.process_lines()

    notion_database = NotionDatabase(access_info)

    txt2notion = Txt2Notion(notion_database, text_loader)

    txt2notion.write_to_notion(start_line=0, frequency=50)