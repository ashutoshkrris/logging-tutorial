import logging
from logging.handlers import TimedRotatingFileHandler

# Set up the logger
logger = logging.getLogger(__name__)

# Create the TimedRotatingFileHandler
handler = TimedRotatingFileHandler(
    filename='myapp.log', when='midnight', backupCount=7)

# Set the log message format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)
