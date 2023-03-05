import sys
import logging
from pythonjsonlogger import jsonlogger

logger = logging.getLogger(__name__)

stdout = logging.StreamHandler(stream=sys.stdout)

format = jsonlogger.JsonFormatter(
    "%(asctime)s | %(levelname)s : %(message)s",
    rename_fields={"levelname": "log_level", "asctime": "timestamp"},
)

stdout.setFormatter(format)
logger.addHandler(stdout)
logger.setLevel(logging.INFO)

try:
    num = int('A')
except ValueError as e:
    logger.error('Failed to convert to int', exc_info=True)
    logger.exception('Failed to convert to int')
