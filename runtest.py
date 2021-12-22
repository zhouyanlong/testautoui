import sys
import subprocess

WIN = sys.platform.startswith('win')


def main():
   """主函数
   使用pytest生成原始报告，里面大多数是一些原始的json数据，加入--clean-alluredir参数清除allure-results历史数据
   使用generate命令导出HTML报告到新的目录
   使用open命令在浏览器中打开HTML报告
   """
   steps = [
       "venv\\Script\\activate" if WIN else "source venv/bin/activate",
       "pytest --alluredir allure-results --clean-alluredir",
       "allure generate allure-results -c -o allure-report",
       "allure open allure-report"
   ]
   for step in steps:
       subprocess.run("call " + step if WIN else step, shell=True)


if __name__ == "__main__":
   main()