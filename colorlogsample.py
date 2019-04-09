import colorlog

logger = colorlog.getLogger()
logger.setLevel(colorlog.colorlog.logging.DEBUG)

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter())
logger.addHandler(handler)

logger.debug("Debug Message")
logger.info("Information Message")
logger.warning("Warning Message")
logger.error("Error Message")
logger.critical("Critical Error")

