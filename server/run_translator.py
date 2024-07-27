from notion_connection.translator_runner import TranslatorRunner
from notion_connection.notion_database import NotionDatabase
from notion_connection.notion_access_info import DatabaseAccessInfo

TARGET_LANGUAGE = 'de'


if __name__ == '__main__':
    access_info = DatabaseAccessInfo()
    access_info.set_access_info_from_dotenv("SECRET_KEY", "DATABASE_ID_TEST")

    notion_database = NotionDatabase(access_info)
    translator_runner = TranslatorRunner(notion_database)
    translator_runner.translate_page_titles(target_language=TARGET_LANGUAGE)