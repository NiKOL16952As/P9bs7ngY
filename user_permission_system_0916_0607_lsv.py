# 代码生成时间: 2025-09-16 06:07:41
import requests
from requests.exceptions import RequestException

# 用户权限管理系统
class UserPermissionSystem:
    """
    用户权限管理系统类，用于管理用户的权限。
    """

    def __init__(self, base_url):
        """
        初始化UserPermissionSystem类。
        :param base_url: REST API的基地址。
        """
        self.base_url = base_url

    def create_user(self, username, password, permissions):
        """
        创建一个新用户。
        :param username: 用户名。
        :param password: 密码。
        :param permissions: 权限列表。
        :return: 响应的JSON数据。
        """
        try:
            url = f"{self.base_url}/users"
            data = {"username": username, "password": password, "permissions": permissions}
            response = requests.post(url, json=data)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"Error creating user: {e}")
            return None

    def get_user(self, user_id):
        """
        根据用户ID获取用户信息。
        :param user_id: 用户ID。
        :return: 响应的JSON数据。
        """
        try:
            url = f"{self.base_url}/users/{user_id}"
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"Error retrieving user: {e}")
            return None

    def update_user_permissions(self, user_id, permissions):
        """
        更新用户的权限。
        :param user_id: 用户ID。
        :param permissions: 新的权限列表。
        :return: 响应的JSON数据。
        """
        try:
            url = f"{self.base_url}/users/{user_id}/permissions"
            data = {"permissions": permissions}
            response = requests.put(url, json=data)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"Error updating user permissions: {e}")
            return None

    def delete_user(self, user_id):
        """
        删除用户。
        :param user_id: 用户ID。
        :return: 响应的JSON数据。
        """
        try:
            url = f"{self.base_url}/users/{user_id}"
            response = requests.delete(url)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"Error deleting user: {e}")
            return None

# 示例用法
if __name__ == '__main__':
    base_url = "http://example.com/api"
    ups = UserPermissionSystem(base_url)

    # 创建用户
    user_id = ups.create_user("john_doe", "password123", ["read", "write"])
    if user_id:
        print(f"User created with ID: {user_id}")

    # 获取用户信息
    user_info = ups.get_user(user_id)
    if user_info:
        print("User info: ", user_info)

    # 更新用户权限
    updated_permissions = ups.update_user_permissions(user_id, ["read", "write", "delete"])
    if updated_permissions:
        print("Updated permissions: ", updated_permissions)

    # 删除用户
    deletion_result = ups.delete_user(user_id)
    if deletion_result:
        print("User deleted: ", deletion_result)