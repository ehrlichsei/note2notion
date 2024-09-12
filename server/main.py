import os 
import logging
import logger_config

from my_timer import Timer
from notion_connection.notion_database import NotionDatabase
from notion_connection.notion_access_info import DatabaseAccessInfo
from notion_connection.txt_loader import TxtLoader
from notion_connection.txt2notion import Txt2Notion
from notion_connection.txt_manager import TxtManager
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Constants for file paths and database IDs
DATABASES = {
    "TEST": "DATABASE_ID_TEST",
    "INSPIRATION_EN": "DATABASE_ID_INSPIRATION_EN",
    "INSPIRATION_DE": "DATABASE_ID_INSPIRATION_DE",
    "ENVIRONMENT_EN": "DATABASE_ID_ENVIRONMENT_EN",
    "TASK_IDEAS_EN": "DATABASE_ID_TASK_IDEAS_EN",
}

# Input paths
INPUT_PATHS = {
    "demo": "data/demo.txt",
    "inspiration_en": "data/inspiration_en.txt",
    "inspiration_de": "data/inspiration_de.txt",
    "environment_en": "data/environment_en.txt",
    "task_ideas_en": "data/task_ideas_en.txt",
}

def load_data_to_database(target_db, input_path):
    # Check if input path exists
    if not os.path.exists(input_path):
        print(f"Error: File '{input_path}' not found.")
        return

    # Simulate file reading
    try:
        with open(input_path, 'r') as file:
            data = file.read()
            # Here you can add logic to load the data into the target database
            print(f"Data from {input_path} successfully loaded into {target_db}")
    except Exception as e:
        print(f"Error reading the file: {e}")


def print_inputs(target_database, input_path):
    logging.info(f"Target database: {target_database}")
    logging.info(f"Input path: {input_path}")


if __name__ == '__main__':

    # Select target database and input path
    TARGET_DATABASE_KEY = os.getenv('TARGET_DATABASE_KEY')
    INPUT_FILE_KEY = os.getenv('INPUT_FILE_KEY')

    # Get database ID and input path
    TARGET_DATABASE = DATABASES.get(TARGET_DATABASE_KEY)
    INPUT_PATH = INPUT_PATHS.get(INPUT_FILE_KEY)

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
