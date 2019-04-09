import logging

logger = logging.getLogger()

logger.info('This is a debug test')
logger.warning("This is a Warning")
logger.error("This is an Error")

try:
  1/0
except:
  logger.exception('We got an exception:')