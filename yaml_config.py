import logging.config
import yaml

with open('config.yaml') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

# Now, log messages using the your own logger
logger = logging.getLogger("my_logger")

# Write messages with all different types of levels
logger.debug('A Debug Message')
logger.info('An Info Message')
logger.warning('A Warning Message')
logger.error('An Error Message')
logger.critical('A Critical Message')
