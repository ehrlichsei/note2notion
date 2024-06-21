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

@app.route("/")
def index():
    return "This is yet another version!"


@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({'message': 'hello world'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=True)