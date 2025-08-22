# 代码生成时间: 2025-08-23 01:05:46
import os
import requests
from PIL import Image
from io import BytesIO

"""
批量图片尺寸调整器
这个脚本使用requests库来获取图片，并使用PIL库来调整图片尺寸。
"""

# 配置
API_URL = "https://api.example.com/images"  # 假设的API端点
IMAGES_DIRECTORY = "./images"  # 存放图片的目录
OUTPUT_DIRECTORY = "./resized_images"  # 调整后图片存放的目录
NEW_SIZE = (800, 600)  # 新的图片尺寸


def download_image(image_url, output_path):
    """
    下载图片并保存
    :param image_url: 图片URL
    :param output_path: 保存路径
    :return: 无
    """
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(response.content)
    else:
        raise Exception(f"Image download failed with status code {response.status_code}")


def resize_image(image_path, output_path, new_size):
    """
    调整图片尺寸
    :param image_path: 原始图片路径
    :param output_path: 输出图片路径
    :param new_size: 新的尺寸
    :return: 无
    """
    with Image.open(image_path) as img:
        img = img.resize(new_size, Image.ANTIALIAS)
        img.save(output_path)


def batch_resize(images):
    """
    批量调整图片尺寸
    :param images: 图片URL列表
    """
    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)  # 确保输出目录存在
    for index, image_url in enumerate(images):
        try:
            # 下载图片
            image_name = os.path.basename(image_url)
            image_path = os.path.join(IMAGES_DIRECTORY, image_name)
            download_image(image_url, image_path)

            # 调整尺寸
            output_path = os.path.join(OUTPUT_DIRECTORY, image_name)
            resize_image(image_path, output_path, NEW_SIZE)
            print(f"Image {index + 1} resized and saved to {output_path}")
        except Exception as e:
            print(f"Error processing image {image_name}: {str(e)}")

# 示例图片URL列表
image_urls = [
    "https://example.com/image1.jpg",
    "https://example.com/image2.jpg",
    # 更多图片URL
]

# 执行批量调整尺寸
batch_resize(image_urls)