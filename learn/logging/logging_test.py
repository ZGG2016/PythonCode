
import logging

# def logger(name):
#     logger_obj = logging.getLogger(name)
#     return logger_obj
#
# print(logger("aaa"))
# print(logger("aaa"))
# print(logger(optexcel.IN))

logger = logging.getLogger("simple_example")
logger.setLevel(logging.DEBUG)

# 建立一个streamhandler来把日志打在CMD窗口上，级别为error以上
sh = logging.StreamHandler()
sh.setLevel(logging.ERROR)
# 建立一个filehandler来把日志记录在文件里，级别为debug以上
fh = logging.FileHandler("logging.log")
fh.setLevel(logging.DEBUG)

format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
sh.setFormatter(format)
fh.setFormatter(format)

logger.addHandler(sh)
logger.addHandler(fh)

logger.debug("debug message")
logger.info("info message")
logger.warning("warn message")
logger.error("error message")
logger.critical("critical message")
