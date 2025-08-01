# 代码生成时间: 2025-08-01 15:10:45
import requests
import random
from flask import Flask, jsonify

# 创建 Flask 应用
app = Flask(__name__)

# 路由：生成随机数
@app.route('/random')
def generate_random_number():
    # 从请求中获取参数
    try:
        min_val = int(request.args.get('min', 0))
        max_val = int(request.args.get('max', 100))
    except ValueError:
        return jsonify({'error': 'Invalid input values. Please use integers.'}), 400
    
    # 检查参数有效性
    if min_val >= max_val:
        return jsonify({'error': 'Min value should be less than max value.'}), 400
    
    # 生成随机数
    random_number = random.randint(min_val, max_val)
    
    # 返回随机数
    return jsonify({'random_number': random_number})

# 运行 Flask 应用
if __name__ == '__main__':
    app.run(debug=True)