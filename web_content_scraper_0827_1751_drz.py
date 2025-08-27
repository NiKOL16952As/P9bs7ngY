# 代码生成时间: 2025-08-27 17:51:08
import requests
from bs4 import BeautifulSoup
import logging

# 设置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class WebContentScraper:
    """网页内容抓取工具"""

    def __init__(self, url):
        """初始化URL"""
        self.url = url

    def fetch_content(self):
        """从给定URL抓取网页内容"""
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # 检查请求是否成功
            return response.text
        except requests.RequestException as e:
            logging.error(f"请求错误：{e}")
            return None

    def parse_content(self, html):
        """解析网页内容"""
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def get_title(self, soup):
        """提取网页标题"""
        return soup.title.string if soup.title else None

    def get_links(self, soup):
        """提取网页中的所有链接"""
        return [a['href'] for a in soup.find_all('a', href=True)]

    def run(self):
        """运行网页内容抓取工具"""
        logging.info(f"开始抓取网页内容：{self.url}")
        html = self.fetch_content()
        if html:
            soup = self.parse_content(html)
            title = self.get_title(soup)
            links = self.get_links(soup)
            logging.info(f"网页标题：{title}")
            logging.info(f"网页链接：{links}")
        else:
            logging.error("网页内容抓取失败")

if __name__ == '__main__':
    # 示例：抓取维基百科首页的内容
    url = "https://www.wikipedia.org/"
    scraper = WebContentScraper(url)
    scraper.run()