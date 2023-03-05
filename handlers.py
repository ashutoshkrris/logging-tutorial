import logging

# Create a custom logger
logger = logging.getLogger('my_module')

# Create a file handler for the logger
handler = logging.FileHandler('my_module.log')

# Add the handler to the logger
logger.addHandler(handler)

# Log a message using the custom logger
logger.warning('This is a log entry for my_module')
