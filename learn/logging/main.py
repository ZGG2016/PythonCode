# logging模块保证在同一个python解释器内，多次调用logging.getLogger('log_name')
# 都会返回同一个logger实例，即使是在多个模块的情况下。所以典型的多模块场景下使用
# logging的方式是在main模块中配置logging，这个配置会作用于多个的子模块，
# 然后在其他模块中直接通过getLogger获取Logger对象即可。


import logging.config
import mod

logging.config.fileConfig('logging.conf')
root_logger = logging.getLogger('root')
root_logger.debug('遇到的坑.md root logger...')

logger = logging.getLogger('main')
logger.info('遇到的坑.md main logger')
logger.info('start import module \'mod\'...')


logger.debug('let\'s 遇到的坑.md mod.testLogger()')
mod.testLogger()

root_logger.info('finish 遇到的坑.md...')