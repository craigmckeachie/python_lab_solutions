from cmath import log
import logging
import os

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG')
logging.basicConfig(level=LOG_LEVEL, format= "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logging.debug('debug message')
logging.info('info message')
logging.warning('warn message')
logging.error('error message')
logging.critical('critical message')

#netinfo subsystem
log = logging.getLogger("netinfo")
log.setLevel(logging.CRITICAL)
log.debug('debug message')
log.info('info message')
log.warning('warn message')
log.error('error message')
log.critical('critical message')