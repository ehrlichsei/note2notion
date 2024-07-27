import os 
import logging
import logger_config

from my_timer import Timer
from notion_connection.notion_database import NotionDatabase
from notion_connection.notion_access_info import DatabaseAccessInfo
from notion_connection.txt_loader import TxtLoader
from notion_connection.txt2notion import Txt2Notion
from notion_connection.txt_manager import TxtManager


TARGET_DATABASE = "DATABASE_ID_TEST"
INPUT_PATH = "data/demo.txt"

def print_inputs(target_database, input_path):
    logging.info(f"Target database: {target_database}")
    logging.info(f"Input path: {input_path}")


if __name__ == '__main__':
    timer = Timer()
    logging.debug("Program started...")

    print_inputs(TARGET_DATABASE, INPUT_PATH)

    access_info = DatabaseAccessInfo()
    access_info.set_access_info_from_dotenv("SECRET_KEY", TARGET_DATABASE)

    timer.start()
    logging.info("First segment starts...")
    text_manager = TxtManager(INPUT_PATH)
    text_manager.remove_blank_lines()
    timer.stop()
    timer.record_timing("First segment")

    text_loader = TxtLoader(INPUT_PATH)
    text_loader.process_lines()

    timer.start()
    logging.info("Second segment starts...")
    notion_database = NotionDatabase(access_info)
    txt2notion = Txt2Notion(notion_database, text_loader)
    timer.stop()
    timer.record_timing("Second segment")

    timer.start()
    logging.info("Third segment starts...")
    txt2notion.write_to_notion(start_line=0, frequency=50)
    timer.stop()
    timer.record_timing("Third segment")

    timer.print_timings()
