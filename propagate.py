import logging

# Create two loggers
logger_a = logging.getLogger('a')
logger_a_b = logging.getLogger('a.b')

# Set the propagate attribute of logger_a to False
logger_a_b.propagate = False

# Create a StreamHandler and set the logging level to INFO
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

# Create a formatter and set the format of handler
format = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
handler.setFormatter(format)

# Add the handler to both loggers
logger_a.addHandler(handler)
logger_a_b.addHandler(handler)

# Log messages
logger_a.warning('warning message from logger_a')
logger_a_b.warning('warning message from logger_a_b')
