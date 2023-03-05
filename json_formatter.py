import sys
import logging
from pythonjsonlogger import jsonlogger

logger = logging.getLogger(__name__)

stdout = logging.StreamHandler(stream=sys.stdout)

format = jsonlogger.JsonFormatter(
    "%(asctime)s | %(levelname)s : %(message)s"
)

stdout.setFormatter(format)
logger.addHandler(stdout)

logger.warning('A Warning Message')
logger.error('An Error Message')
logger.critical('A Critical Message')
