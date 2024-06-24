# logger_config.py
import logging

# 配置日志格式
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'

# 配置日志级别，默认为DEBUG
LOG_LEVEL = logging.INFO

# 设置全局日志对象
logging.basicConfig(format=LOG_FORMAT, level=LOG_LEVEL)

# 如果需要输出到文件，可以添加FileHandler等配置
# logging.FileHandler("app.log")
