import sys
import logging

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger("balmersparty")

requests_logger = logging.getLogger('engineio')
requests_logger.setLevel(logging.WARNING)
