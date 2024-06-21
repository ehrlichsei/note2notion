from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os

from server.notion_connection.txt2notion import Txt2Notion
from server.notion_connection.notion_database import NotionDatabase
from server.notion_connection.notion_access_info import DatabaseAccessInfo
from server.notion_connection.txt_loader import TxtLoader

app = Flask(__name__)
CORS(app)

access_info = DatabaseAccessInfo()
access_info.set_access("SECRET_KEY", "DATABASE_ID_TEST")
filepath = "deploy_test.txt"
access_info.print_access_info()

text_loader = TxtLoader(filepath)
text_loader.process_lines()

notion_database = NotionDatabase(access_info)
notion_database.test_connection()

txt2notion = Txt2Notion(notion_database, text_loader)
print("intialized txt2notion")

# 上传文件存储目录
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
ALLOWED_EXTENSIONS = {'txt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/write2notion', methods=['GET'])
def write2notion():
    print("writing to notion")
    txt2notion.write_to_notion(start_line=0, frequency=50)
    print("wrote to notion")
    return jsonify({'message': 'Writing to notion successful'})

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

@app.route('/api/upload', methods=['POST'])
def upload_file():
    # 检查请求是否包含文件
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    # 如果用户未选择文件，浏览器也会发送一个空的文件部分
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # 检查文件扩展名
    if file and allowed_file(file.filename):
        # 将文件保存到指定路径
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        # 对上传的文件进行处理，比如读取内容并返回
        with open(file_path, 'r', encoding='utf-8') as f:
            file_content = f.read()

        # 解码成中文文本
        file_content_decoded = file_content.encode('utf-8').decode('unicode-escape')

        # 返回上传成功的信息及文件内容（示例）
        return jsonify({'message': 'File uploaded successfully', 'file_content': file_content_decoded}), 200

    else:
        return jsonify({'error': 'Invalid file type'}), 400

@app.route("/")
def index():
    return "This is yet another version!"


@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({'message': 'hello world'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5002))
    app.run(host='0.0.0.0', port=port, debug=True)