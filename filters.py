import logging


class RecordFilter(logging.Filter):
    def filter(self, record):
        return record.msg.startswith('Important:')


logger = logging.getLogger('filtered_logger')
handler = logging.FileHandler('filtered_log.log')
handler.setFormatter(logging.Formatter(
    '%(asctime)s | %(levelname)s : %(message)s'))
handler.addFilter(RecordFilter())
logger.addHandler(handler)

logger.warning('Important: This message should be logged')
logger.warning('This message should not be logged')
