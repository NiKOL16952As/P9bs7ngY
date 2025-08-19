# 代码生成时间: 2025-08-19 16:51:52
import requests
import json
import os

class ConfigManager:
    """配置文件管理器，用于读取和更新配置文件。"""

    def __init__(self, config_url):
        """初始化配置文件管理器。

        :param config_url: 配置文件的URL。
        """
        self.config_url = config_url

    def fetch_config(self):
        """从指定URL获取配置文件。

        :return: 配置文件的内容，格式为JSON。
        :raises: requests.RequestException
        """
        try:
            response = requests.get(self.config_url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching config: {e}")
            raise

    def update_config(self, new_config):
        """更新配置文件。

        :param new_config: 新的配置内容，格式为JSON。
        :raises: requests.RequestException
        """
        try:
            response = requests.put(self.config_url, json=new_config)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error updating config: {e}")
            raise

    def save_config(self, config_data, local_path):
        """将配置文件保存到本地。

        :param config_data: 配置文件的内容，格式为JSON。
        :param local_path: 本地文件路径。
        """
        try:
            with open(local_path, 'w') as f:
                json.dump(config_data, f, indent=4)
        except IOError as e:
            print(f"Error saving config: {e}")
            raise

# 示例用法
if __name__ == '__main__':
    config_url = "http://example.com/config.json"
    local_path = "./config.json"
    config_manager = ConfigManager(config_url)

    try:
        # 获取配置文件
        config_data = config_manager.fetch_config()
        print("Config fetched successfully")
        print(config_data)

        # 更新配置文件
        new_config = {"key": "value"}
        updated_config = config_manager.update_config(new_config)
        print("Config updated successfully")
        print(updated_config)

        # 保存配置文件到本地
        config_manager.save_config(config_data, local_path)
        print("Config saved to local")
    except Exception as e:
        print(f"An error occurred: {e}")