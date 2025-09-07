# 代码生成时间: 2025-09-07 23:06:59
import requests
import json
import datetime

class TestReportGenerator:
    def __init__(self, base_url):
        """
        初始化测试报告生成器

        :param base_url: 测试服务的基础URL
        """
        self.base_url = base_url
        self.headers = {"Content-Type": "application/json"}

    def generate_test_report(self, test_case_id):
        """
        根据测试用例ID生成测试报告

        :param test_case_id: 测试用例的ID
        :return: 测试报告的内容或错误信息
        """
        try:
            # 构建请求URL
            url = f"{self.base_url}/tests/{test_case_id}/report"
            # 发送GET请求
            response = requests.get(url, headers=self.headers)
            # 检查响应状态码
            if response.status_code == 200:
                # 解析测试报告
                report_content = response.json()
                return report_content
            else:
                # 返回错误信息
                return {
                    "error": f"Failed to generate report. Status code: {response.status_code}",
                    "message": response.text
                }
        except requests.exceptions.RequestException as e:
            # 处理请求异常
            return {"error": "Request exception occurred", "message": str(e)}

    def save_test_report(self, report_content, report_name):
        """
        将测试报告保存到文件

        :param report_content: 测试报告的内容
        :param report_name: 报告文件的名称
        :return: 保存结果
        """
        try:
            # 创建文件并写入报告内容
            with open(report_name, 'w') as f:
                json.dump(report_content, f, indent=4)
            return {"message": "Test report saved successfully"}
        except IOError as e:
            # 处理文件写入异常
            return {"error": "Failed to save test report", "message": str(e)}

# 使用示例
if __name__ == '__main__':
    base_url = "http://example.com/api"
    test_case_id = 123
    report_name = f"test_report_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.json"

    generator = TestReportGenerator(base_url)
    report_content = generator.generate_test_report(test_case_id)
    if 'error' not in report_content:
        save_result = generator.save_test_report(report_content, report_name)
        print(save_result)
    else:
        print(report_content)