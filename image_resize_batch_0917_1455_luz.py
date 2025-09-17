# 代码生成时间: 2025-09-17 14:55:31
import os
from PIL import Image
import requests
from io import BytesIO

"""
图片尺寸批量调整器

该脚本使用PIL库进行图片尺寸调整，支持从本地目录或网络URL批量读取图片，并将调整后的图片保存到指定目录。
"""

class ImageResizeBatch:
    def __init__(self, input_dir, output_dir, target_size):
        """初始化图片尺寸批量调整器
        
        :param input_dir: 输入目录，包含待处理的图片文件
        :param output_dir: 输出目录，调整后的图片将保存在此目录
        :param target_size: 目标尺寸，元组形式（宽，高）
        """
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.target_size = target_size
        
    def resize_image(self, image_path):
        """调整单个图片尺寸
        
        :param image_path: 图片文件路径
        :return: 调整后的图片数据
        """
        try:
            with Image.open(image_path) as img:
                img = img.resize(self.target_size)
                return img
        except IOError:
            print(f"Error resizing image {image_path}")
            return None
    
    def save_image(self, img, output_path):
        "