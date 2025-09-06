# 代码生成时间: 2025-09-07 06:53:43
import requests
import json
import random

"""
测试数据生成器，用于生成测试数据并发送POST请求。

Attributes:
    None

Methods:
    generate_random_data: 生成随机测试数据。
    send_post_request: 发送POST请求，携带测试数据。
"""

class TestDataGenerator:
    def __init__(self, url):
        """
        初始化测试数据生成器。
        
        Args:
            url (str): 目标URL。
        """
        self.url = url

    def generate_random_data(self):
        """
        生成随机测试数据。
        
        Returns:
            dict: 随机生成的测试数据。
        """
        data = {
            'id': random.randint(1, 100),  # 随机ID
            'name': f'User{random.randint(1, 100)}',  # 随机用户名
            'age': random.randint(18, 80),  # 随机年龄
            'gender': random.choice(['Male', 'Female', 'Other']),  # 随机性别
            'email': f'user{random.randint(1, 100)}@example.com'  # 随机邮箱
        }
        return data

    def send_post_request(self, data):
        """
        发送POST请求，携带测试数据。
        
        Args:
            data (dict): 测试数据。
        
        Returns:
            response: 请求响应对象。
        """
        try:
            response = requests.post(self.url, json=data)
            response.raise_for_status()  # 检查请求是否成功
            return response
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except requests.exceptions.RequestException as err:
            print(f'Other error occurred: {err}')
        except Exception as err:
            print(f'An unexpected error occurred: {err}')


def main():
    """
    主函数，用于测试数据生成器。
    """
    # 设置目标URL
    target_url = 'http://example.com/api/submit'
    
    # 创建测试数据生成器实例
    generator = TestDataGenerator(target_url)
    
    # 生成随机测试数据
    random_data = generator.generate_random_data()
    print(f'Generated Test Data: {random_data}')
    
    # 发送POST请求并获取响应
    response = generator.send_post_request(random_data)
    if response:
        print(f'Response Status Code: {response.status_code}')
        print(f'Response Content: {response.json()}')

if __name__ == '__main__':
    main()