import logging
import logging.config

# Declare handlers, formatters and all functions using dictionary 'key' : 'value' pair
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'consoleFormatter': {
            'format': '%(asctime)s | %(name)s | %(levelname)s : %(message)s',
        },
        'fileFormatter': {
            'format': '%(asctime)s | %(name)s | %(levelname)s : %(message)s',
        },
    },
    'handlers': {
        'file': {
            'filename': 'debug.log',
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'fileFormatter',
        },
        'console': {
            'level': 'CRITICAL',
            'class': 'logging.StreamHandler',
            'formatter': 'consoleFormatter',
        },
    },
    'loggers': {
        '': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
        },
    },
})

# Define your own logger name
logger = logging.getLogger("my_logger")

# Write messages with all different types of levels
logger.debug('A Debug Message')
logger.info('An Info Message')
logger.warning('A Warning Message')
logger.error('An Error Message')
logger.critical('A Critical Message')
