from flask import Flask, jsonify, request
from notion_connection.txt2notion import Txt2Notion
from notion_connection.notion_database import NotionDatabase
from notion_connection.notion_access_info import DatabaseAccessInfo
from notion_connection.txt_loader import TxtLoader

app = Flask(__name__)

access_info = DatabaseAccessInfo()
access_info.set_access_info_from_dotenv("SECRET_KEY", "DATABASE_ID_TEST")
filepath = "demo.txt"

text_loader = TxtLoader(filepath)
text_loader.process_lines()

notion_database = NotionDatabase(access_info)
notion_database.test_connection()

txt2notion = Txt2Notion(notion_database, text_loader)
print("intialized txt2notion")

@app.route('/api/write2notion', methods=['GET'])
def write2notion():
    print("writing to notion")
    txt2notion.write_to_notion(start_line=0, frequency=50)
    print("wrote to notion")
    return jsonify({'message': 'Writing to notion successful'})

@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({'message': 'hello world'})

@app.route('/api/submit', methods=['POST'])
def submit_url():
    if request.method == 'POST':
        # 获取 POST 请求中的数据
        name = request.args.get('name')
        email = request.args.get('email')
        print(name, email)

        # 做一些处理逻辑，比如存储到数据库或者进行其他操作
        # 这里简单返回一个响应
        response = {
            'message': 'Received data',
            'name': name,
            'email': email
        }
        return jsonify(response)
    
@app.route('/api/submit_json', methods=['POST'])
def submit_json():
    if request.method == 'POST':
        # 获取 POST 请求中的 JSON 数据
        data = request.json
        name = data.get('name')
        email = data.get('email')
        print(name, email)

        # 做一些处理逻辑，比如存储到数据库或者进行其他操作
        # 这里简单返回一个响应
        response = {
            'message': 'Received data',
            'name': name,
            'email': email
        }
        return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)  # 启动 Flask 应用的调试模式