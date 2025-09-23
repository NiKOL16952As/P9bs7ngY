# 代码生成时间: 2025-09-23 09:49:06
import requests

"""
RESTful API接口开发

该模块提供了一个简单的RESTful API接口客户端，使用requests库与API服务器进行交互。
"""

def get_api_data(url):
    """
    向指定的URL发送GET请求，并返回响应内容。

    :param url: API的URL地址
    :return: API响应的JSON数据
    :raises: requests.RequestException
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # 触发HTTPError异常，如果状态码不是200
        return response.json()
    except requests.RequestException as e:
        print(f"请求失败：{e}")
        return None


def post_api_data(url, data):
    """
    向指定的URL发送POST请求，并返回响应内容。

    :param url: API的URL地址
    :param data: 要发送的数据，应为字典格式
    :return: API响应的JSON数据
    :raises: requests.RequestException
    """
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # 触发HTTPError异常，如果状态码不是200
        return response.json()
    except requests.RequestException as e:
        print(f"请求失败：{e}")
        return None

# 示例用法
if __name__ == '__main__':
    api_url = "http://example.com/api/"
    get_response = get_api_data(api_url)
    if get_response:
        print("GET请求响应：", get_response)
    else:
        print("GET请求失败。")

    post_data = {"key": "value"}
    post_response = post_api_data(api_url, post_data)
    if post_response:
        print("POST请求响应：", post_response)
    else:
        print("POST请求失败。")