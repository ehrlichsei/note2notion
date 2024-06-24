from notion.client import NotionClient
# from dotenv import load_dotenv
# import os

# dotenv.load_dotenv()

# secret_key = os.getenv('SECRET_KEY')
# access_id = os.getenv('PAGE_ID_TEST')

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in (non-guest) session on Notion.so
client = NotionClient('APITOKEN')

# Replace this URL with the URL of the page you want to edit
page = client.get_block("page_URL")

print("The old title is:", page.title)

# Note: You can use Markdown! We convert on-the-fly to Notion's internal formatted text data structure.
page.title = "The title has now changed, and has *live-updated* in the browser!"