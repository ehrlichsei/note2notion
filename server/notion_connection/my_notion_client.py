import os
from notion_client import Client

notion = Client(auth="APITOKEN")

from pprint import pprint

response = notion.databases.list()
pprint(response)