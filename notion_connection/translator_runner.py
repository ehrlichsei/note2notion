from notion_access_info import DatabaseAccessInfo
from notion_database import NotionDatabase
from translator import translate_text

class TranslatorRunner:

    def __init__(self, notion_database: NotionDatabase):
        self.notion_database = notion_database

    def translate_page_titles(self, target_language='en'):
        for page in self.notion_database.pages:
            current_title = page.get_page_name()
            translated_title = translate_text(current_title, target=target_language)
            print(f"Current title of page '{current_title}': {translated_title}")
            if translated_title != current_title:
                page.update_title(translated_title)
                print(f"Translated title of page '{current_title}' to '{translated_title}'")

# 示例用法
if __name__ == '__main__':
    access_info = DatabaseAccessInfo()
    access_info.set_access_info_from_dotenv("SECRET_KEY", "DATABASE_ID_TEST")

    notion_database = NotionDatabase(access_info)
    translator_runner = TranslatorRunner(notion_database)

    translator_runner.translate_page_titles(target_language='ru')
