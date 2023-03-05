import logging

# Create a custom logger
logger = logging.getLogger('example')

# Create a file handler for the logger
handler = logging.FileHandler('example.log')

format = logging.Formatter(
    "%(asctime)s | %(name)s | %(levelname)s : %(message)s"
)

handler.setFormatter(format)

# Add the handler to the logger
logger.addHandler(handler)

# Log a message using the custom logger
logger.critical('This is a log entry for example')
