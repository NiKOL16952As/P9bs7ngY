# 代码生成时间: 2025-09-10 02:46:15
import requests
import json

"""
API响应格式化工具，用于接收API响应并格式化输出。

功能：
- 发送GET请求到指定的API端点
- 解析响应内容
- 将解析后的内容格式化输出

使用方法：
- 指定API端点和所需的参数
- 调用format_api_response函数
"""


def format_api_response(url, params=None):
    """
    格式化API响应工具函数。
    
    参数：
    url (str): API端点的URL。
    params (dict): 要发送到API端点的参数。默认为None。
    
    返回：
    格式化后的API响应内容。
    
    异常：
    - requests.RequestException：网络请求异常。
    - json.JSONDecodeError：JSON解析异常。
    """
    try:
        # 发送GET请求到API端点
        response = requests.get(url, params=params)
        # 确保响应状态码为200
        response.raise_for_status()
        # 尝试解析JSON响应内容
        data = response.json()
        # 格式化输出响应内容
        return json.dumps(data, indent=4, ensure_ascii=False)
    except requests.RequestException as e:
        # 处理网络请求异常
        return {
            'error': '网络请求异常',
            'message': str(e)
        }
    except json.JSONDecodeError as e:
        # 处理JSON解析异常
        return {
            'error': 'JSON解析异常',
            'message': str(e)
        }
    except Exception as e:
        # 处理其他异常
        return {
            'error': '未知异常',
            'message': str(e)
        }

# 示例用法
if __name__ == '__main__':
    # 指定API端点和参数
    url = 'https://api.example.com/data'
    params = {'key': 'value'}
    
    # 调用函数并打印格式化后的结果
    result = format_api_response(url, params)
    print(result)