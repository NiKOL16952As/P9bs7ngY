# 代码生成时间: 2025-08-12 05:53:10
import requests
from getpass import getpass
import json

"""
Interactive Chart Generator

This script uses the Plotly API to create interactive charts.
It allows users to input data and chart type, then generates
the corresponding chart and saves it as a .html file.
"""

class InteractiveChartGenerator:
    def __init__(self):
        self.plotly_api_key = self._get_plotly_api_key()
        self.chart_data = {}
        self.chart_type = ""
        self.output_file = ""

    def _get_plotly_api_key(self):
        "