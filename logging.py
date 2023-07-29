import sys

def functc():
    print(sys._getframe().f_code.co_name)

functc()

import logging
logger = logging.getLogger("Testing logs")
logger.debug("1")
logger.info("2")
logger.warning("3")
logger.error("4")
logger.critical("5")
