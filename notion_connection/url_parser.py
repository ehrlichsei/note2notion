# parse notion url to get page id or database id

def parse_notion_url(url):
    content = url.split('/')[-1]
    return content


def parse_page_id(url):
    page_id = parse_notion_url(url)
    return page_id

def parse_database_id(url):
    database_url = parse_notion_url(url)
    database_id = database_url.split('?')[0]
    return database_id


if __name__ == '__main__':
    database_url = "https://www.notion.so/kittybro/983741b3cb5c45798d439bb2f958e5a6?v=3deac939066842e691cb987abb9a6902"
    print(parse_database_id(database_url))

    page_url = "https://www.notion.so/kittybro/1-1b88bfc6d2674ef79ecadab820ded431"
    print(parse_page_id(page_url))