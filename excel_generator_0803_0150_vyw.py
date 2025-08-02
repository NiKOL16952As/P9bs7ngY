# 代码生成时间: 2025-08-03 01:50:13
import openpyxl
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import pandas as pd

class ExcelGenerator:
    """
    自动生成Excel表格的类。
    """
    def __init__(self, filename='Generated_Excel.xlsx', sheet_name='Sheet1'):
        """
        初始化ExcelGenerator类。
        :param filename: Excel文件名。
        :param sheet_name: 工作表名。
        """
        self.filename = filename
        self.sheet_name = sheet_name
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.title = sheet_name

    def add_header(self, header):
        """
        添加表头。
        :param header: 表头列表。
        """
        self.ws.append(header)

    def add_row(self, row):
        """
        添加一行数据。
        :param row: 一行数据列表。
        """
        self.ws.append(row)

    def add_dataframe(self, df):
        """
        从Pandas DataFrame添加数据。
        :param df: Pandas DataFrame对象。
        """
        for r in dataframe_to_rows(df, index=False, header=True):
            self.ws.append(r)

    def save(self):
        """
        保存Excel文件。
        """
        try:
            self.wb.save(filename=self.filename)
            print(f'Excel文件已保存为：{self.filename}')
        except Exception as e:
            print(f'保存Excel文件时发生错误：{e}')

    def load_from_file(self, filepath):
        """
        从现有文件加载Excel数据。
        :param filepath: Excel文件路径。
        """
        try:
            self.wb = openpyxl.load_workbook(filepath)
            self.ws = self.wb[self.sheet_name]
        except FileNotFoundError:
            print(f'文件未找到：{filepath}')
        except Exception as e:
            print(f'加载Excel文件时发生错误：{e}')

# 示例使用
if __name__ == '__main__':
    # 创建ExcelGenerator实例
    excel_generator = ExcelGenerator('Sample_Excel.xlsx', 'SampleSheet')

    # 添加表头
    excel_generator.add_header(['Name', 'Age', 'City'])

    # 添加数据行
    excel_generator.add_row(['Alice', 25, 'New York'])
    excel_generator.add_row(['Bob', 30, 'Los Angeles'])

    # 从Pandas DataFrame添加数据
    data = {'Name': ['Charlie', 'David'], 'Age': [28, 35], 'City': ['Chicago', 'Houston']}
    df = pd.DataFrame(data)
    excel_generator.add_dataframe(df)

    # 保存Excel文件
    excel_generator.save()