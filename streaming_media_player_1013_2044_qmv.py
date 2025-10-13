# 代码生成时间: 2025-10-13 20:44:44
import requests
from flask import Flask, Response, render_template, request, send_from_directory
import os
import threading

# 设置流媒体文件夹
STREAM_DIR = "streaming"
APP_DIR = os.path.dirname(os.path.abspath(__file__))
STREAM_PATH = os.path.join(APP_DIR, STREAM_DIR)

# 创建 Flask 应用
app = Flask(__name__)

# 定义一个函数生成器，用于生成流媒体数据流
def generate_streaming_data(stream_url):
    with requests.get(stream_url, stream=True) as response:
        if response.status_code == 200:
            try:
                while True:
                    # 读取数据流
                    chunk = response.raw.read(1024 * 1024)
                    if not chunk:
                        break
                    yield chunk
            except Exception as e:
                print(f"Error occurred while streaming: {e}")
        else:
            print(f"Failed to fetch stream: Status code {response.status_code}")

# 定义路由：播放流媒体
@app.route("/play/<stream_url>")
def play_stream(stream_url):
    # 使用 Response 对象包装数据流生成器
    return Response(generate_streaming_data(stream_url),
                    mimetype='video/mp4')

# 定义路由：播放流媒体文件
@app.route("/<filename>")
def play_file(filename):
    # 检查文件是否存在
    if not os.path.isfile(os.path.join(STREAM_PATH, filename)):
        return f"File {filename} not found.", 404
    # 使用 send_from_directory 发送文件
    return send_from_directory(STREAM_PATH, filename)

# 定义路由：上传流媒体文件
@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]
    if not file:
        return "No file part", 400
    if file.filename == "":
        return "No selected file", 400
    if file:
        # 保存文件到流媒体文件夹
        file.save(os.path.join(STREAM_PATH, file.filename))
        return "File uploaded successfully.", 200

# 定义路由：首页，显示所有流媒体文件
@app.route("/")
def index():
    files = os.listdir(STREAM_PATH)
    return render_template("index.html", files=files)

# 定义路由：下载流媒体文件
@app.route("/download/<filename>")
def download_file(filename):
    # 检查文件是否存在
    if not os.path.isfile(os.path.join(STREAM_PATH, filename)):
        return f"File {filename} not found.", 404
    # 使用 send_from_directory 发送文件
    return send_from_directory(STREAM_PATH, filename, as_attachment=True)

# 启动 Flask 应用
if __name__ == '__main__':
    # 使用线程启动 Flask 应用，以便在后台运行
    thread = threading.Thread(target=app.run, kwargs={"debug": True})
    thread.start()
    print("Flask application is running in the background...")
