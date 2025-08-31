# 代码生成时间: 2025-09-01 05:04:58
import requests

class UserPermissionManager:
    """
    用户权限管理系统。
    """

    def __init__(self, base_url):
        """
        初始化UserPermissionManager类。
        
        :param base_url: 权限服务的基础URL。
        """
        self.base_url = base_url

    def get_user_permissions(self, user_id):
        """
        根据用户ID获取用户的权限列表。
        
        :param user_id: 用户的唯一标识符。
        :return: 权限列表。
        """
        try:
            response = requests.get(f"{self.base_url}/users/{user_id}/permissions")
            response.raise_for_status()  # 检查HTTP响应状态
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"请求错误: {e}")
            return None

    def add_user_permission(self, user_id, permission):
        """
        为用户添加权限。
        
        :param user_id: 用户的唯一标识符。
        :param permission: 要添加的权限。
        :return: 操作结果。
        """
        try:
            response = requests.post(
                f"{self.base_url}/users/{user_id}/permissions",
                json={'permission': permission}
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"请求错误: {e}")
            return None

    def remove_user_permission(self, user_id, permission):
        """
        移除用户的权限。
        
        :param user_id: 用户的唯一标识符。
        :param permission: 要移除的权限。
        :return: 操作结果。
        """
        try:
            response = requests.delete(
                f"{self.base_url}/users/{user_id}/permissions/{permission}"
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"请求错误: {e}")
            return None

# 使用示例
if __name__ == '__main__':
    manager = UserPermissionManager("http://example.com/api")
    
    # 获取用户权限
    permissions = manager.get_user_permissions(1)
    print(permissions)
    
    # 为用户添加权限
    result = manager.add_user_permission(1, "read")
    print(result)
    
    # 移除用户权限
    result = manager.remove_user_permission(1, "write")
    print(result)