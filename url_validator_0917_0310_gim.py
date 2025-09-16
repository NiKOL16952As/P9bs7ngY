# 代码生成时间: 2025-09-17 03:10:18
import requests

"""
URL链接有效性验证程序
"""

def validate_url(url):
    """
    验证给定的URL是否有效。

    :param url: 待验证的URL字符串
    :return: 布尔值，True表示URL有效，False表示无效
    """
    try:
        # 使用GET请求访问URL
        response = requests.get(url)
        # 如果HTTP状态码为200，表示URL有效
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        # 打印异常信息
        print(f"请求异常: {e}")
        return False


def main():
    # 待验证的URL列表
    urls = [
        "http://www.google.com",
        "https://www.example.com",
        "https://www.invalid-url",
    ]

    # 遍历URL列表，验证每个URL的有效性
    for url in urls:
        print(f"验证URL: {url}")
        is_valid = validate_url(url)
        print(f"{url} 是否有效：{'有效' if is_valid else '无效'}")


def __name__ == '__main__':
    main()
