import requests
from requests.auth import HTTPBasicAuth
import json

def get_jira_issue(jira_url, issue_key, username, api_token):
    """
    获取Jira中的issue信息

    参数:
    jira_url (str): Jira实例的基本URL (例如: "https://your-domain.atlassian.net")
    issue_key (str): 要获取的issue的key (例如: "PROJ-123")
    username (str): Jira用户名
    api_token (str): Jira API token

    返回:
    dict: 包含issue信息的字典
    """
    url = f"{jira_url}/rest/api/2/issue/{issue_key}"

    # 使用基本认证
    auth = HTTPBasicAuth(username, api_token)

    # 发送GET请求
    response = requests.get(url, auth=auth)

    # 检查响应状态码
    if response.status_code == 200:
        # 解析JSON响应
        issue_data = response.json()
        return issue_data
    else:
        print(f"获取issue失败，状态码: {response.status_code}")
        print(response.text)
        return None

# 示例使用
jira_url = "https://your-domain.atlassian.net"
issue_key = "PROJ-123"
username = "your-username"
api_token = "your-api-token"

issue = get_jira_issue(jira_url, issue_key, username, api_token)
if issue:
    print(json.dumps(issue, indent=2))
