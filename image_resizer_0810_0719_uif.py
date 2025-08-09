# 代码生成时间: 2025-08-10 07:19:47
import os
import requests
# 添加错误处理
from PIL import Image
from io import BytesIO

"""
Image Resizer: A program to batch resize images using Python and PIL.

Features:
- Reads images from a specified directory.
# 改进用户体验
- Resizes images to a specified width and height while maintaining aspect ratio.
- Saves resized images to a new directory.
- Provides error handling for file operations and image processing.
# 扩展功能模块
"""

class ImageResizer:
# 改进用户体验
    def __init__(self, input_dir, output_dir, target_width, target_height):
        """
        Initialize the ImageResizer with input and output directories,
        and the target width and height for resizing.
        """
        self.input_dir = input_dir
# 增强安全性
        self.output_dir = output_dir
        self.target_width = target_width
# 改进用户体验
        self.target_height = target_height

    def resize_image(self, image_path):
        """
        Resize an individual image while maintaining its aspect ratio.
        """
# NOTE: 重要实现细节
        try:
            with Image.open(image_path) as img:
                # Calculate new dimensions while maintaining aspect ratio
# NOTE: 重要实现细节
                width, height = img.size
# 添加错误处理
                aspect_ratio = width / height
                new_width = min(self.target_width, width)
                new_height = new_width / aspect_ratio

                # Resize the image
                img = img.resize((int(new_width), int(new_height)), Image.ANTIALIAS)

                # Save the resized image
# FIXME: 处理边界情况
                output_path = os.path.join(self.output_dir, os.path.basename(image_path))
                img.save(output_path)
                print(f'Resized image saved to {output_path}')
        except IOError as e:
            print(f'Error resizing image {image_path}: {e}')

    def batch_resize(self):
        """
        Batch resize all images in the input directory.
        """
        if not os.path.exists(self.output_dir):
# 增强安全性
            os.makedirs(self.output_dir)
# 增强安全性

        for filename in os.listdir(self.input_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
# 优化算法效率
                image_path = os.path.join(self.input_dir, filename)
                self.resize_image(image_path)
            else:
                print(f'Skipped non-image file: {filename}')

# Example usage:
if __name__ == '__main__':
    input_directory = 'path/to/input/directory'
    output_directory = 'path/to/output/directory'
    target_width = 800  # Target width for resized images
# 改进用户体验
    target_height = 600  # Target height for resized images
# 扩展功能模块

    resizer = ImageResizer(input_directory, output_directory, target_width, target_height)
    resizer.batch_resize()