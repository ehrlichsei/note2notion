from notion_access_info import PageAccessInfo
from notion_page import NotionPage

import os
from google.cloud import translate_v2 as translate

# 指定凭证文件路径
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/yulifang/.config/gcloud/application_default_credentials.json"

def translate_text(text, target='en'):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target)
    return result['translatedText']


if __name__ == '__main__':
    # 示例用法
    text_to_translate = "прошлые ошибки в обучении "
    translated_text = translate_text(text_to_translate, target='zh')
    print(translated_text)

    access_info = PageAccessInfo()
    access_info.set_access_info_from_dotenv('SECRET_KEY', 'PAGE_ID_TEST')
    page = NotionPage(access_info)
    page.test_connection()
    print(page._get_page_name())

    properties = {
        "Name": {
            "title": [
                {
                    "text": {
                        "content": translated_text  # 替换为你的页面标题内容
                    }
                }
            ]
        }
    }

    print(properties)
    print(properties['Name']['title'][0]['text']['content'])

    page.update_page_property(properties)
