__author__ = "JJ.sven"

import logging
import logging.config

''' log 可以用文件形式配置
    
    propagete为1表示message必须传播到上一级logger中
    
    'https://docs.python.org/2/library/logging.config.html#logging-config-fileformat'
'''

logging.config.fileConfig('log_config')
lg = logging.getLogger('simpleExample')

lg.info('info msg')
lg.debug('debug msg')
lg.warning('warning msg')
lg.error('error msg')

