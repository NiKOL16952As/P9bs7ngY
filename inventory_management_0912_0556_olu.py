# 代码生成时间: 2025-09-12 05:56:53
import requests

class InventoryManagement:
    """
    库存管理系统
    """
    def __init__(self, base_url):
        """
        初始化库存管理系统
        :param base_url: API的基础URL
        """
        self.base_url = base_url

    def get_inventory(self, product_id):
        """
        获取单个产品的库存信息
        :param product_id: 产品ID
        :return: JSON格式的库存信息
        """
        try:
            url = f"{self.base_url}/inventory/{product_id}"
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"请求失败：{e}")
            return None

    def update_inventory(self, product_id, quantity):
        """
        更新产品的库存数量
        :param product_id: 产品ID
        :param quantity: 更新后的数量
        :return: 更新结果
        """
        try:
            url = f"{self.base_url}/inventory/{product_id}"
            data = {"quantity": quantity}
            response = requests.put(url, json=data)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"请求失败：{e}")
            return None

    def add_product(self, product_id, name, quantity):
        """
        添加新产品
        :param product_id: 产品ID
        :param name: 产品名称
        :param quantity: 初始库存数量
        :return: 添加结果
        """
        try:
            url = f"{self.base_url}/products"
            data = {"product_id": product_id, "name": name, "quantity": quantity}
            response = requests.post(url, json=data)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"请求失败：{e}")
            return None

# 示例用法
if __name__ == "__main__":
    inventory = InventoryManagement("http://api.example.com")
    print(inventory.get_inventory("123"))
    print(inventory.update_inventory("123", 10))
    print(inventory.add_product("456", "New Product", 5))
