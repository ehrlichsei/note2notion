import os 
import logging
import logger_config

from my_timer import Timer
from notion_connection.notion_database import NotionDatabase
from notion_connection.notion_access_info import DatabaseAccessInfo
from notion_connection.txt_loader import TxtLoader
from notion_connection.txt2notion import Txt2Notion
from notion_connection.txt_manager import TxtManager


def print_inputs(target_database, input_path):
    logging.info(f"目标数据库: {target_database}")
    logging.info(f"输入文件路径: {input_path}")


if __name__ == '__main__':
    timer = Timer()
    logging.debug("程序开始运行...")

    target_database = "DATABASE_ID_INSPIRATION"
    input_path = "data/demo.txt"
    print_inputs(target_database, input_path)

    access_info = DatabaseAccessInfo()
    access_info.set_access_info_from_dotenv("SECRET_KEY", target_database)

    timer.start()
    logging.info("第一段程序开始运行...")
    text_manager = TxtManager(input_path)
    text_manager.remove_blank_lines()
    timer.stop()
    timer.record_timing("第一段")

    text_loader = TxtLoader(input_path)
    text_loader.process_lines()

    timer.start()
    logging.info("第二段程序开始运行...")
    notion_database = NotionDatabase(access_info)
    txt2notion = Txt2Notion(notion_database, text_loader)
    timer.stop()
    timer.record_timing("第二段")

    timer.start()
    logging.info("第三段程序开始运行...")
    txt2notion.write_to_notion(start_line=0, frequency=50)
    timer.stop()
    timer.record_timing("第三段")

    timer.print_timings()
