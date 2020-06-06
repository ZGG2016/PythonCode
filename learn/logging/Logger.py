
import logging

class Logger:
    def __init__(self,path,clevel=logging.DEBUG,flevel=logging.DEBUG):
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')

        sh = logging.StreamHandler()
        sh.setLevel(clevel)
        sh.setFormatter(fmt)

        fh = logging.FileHandler(path)
        fh.setLevel(flevel)
        fh.setFormatter(fmt)

        self.logger.addHandler(sh)
        self.logger.addHandler(fh)


    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)


if __name__ == '__main__':

    logyyx = Logger('yyx.log', logging.ERROR, logging.DEBUG)
    logyyx.debug('一个debug信息')
    logyyx.info('一个info信息')
    logyyx.warning('一个warning信息')
    logyyx.error('一个error信息')
    logyyx.critical('一个致命critical信息')