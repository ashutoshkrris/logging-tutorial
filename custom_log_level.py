import logging

# Define the custom log level
VERBOSE = 15
logging.VERBOSE = VERBOSE
logging.addLevelName(logging.VERBOSE, 'VERBOSE')


# Set up basic logging configuration for the root logger
logging.basicConfig(level=logging.DEBUG)


# Define a custom logging method for the new level
def verbose(self, message, *args, **kwargs):
    if self.isEnabledFor(logging.VERBOSE):
        self._log(logging.VERBOSE, message, args, **kwargs)


# Add the custom logging method to the logger class
logging.Logger.verbose = verbose

# Create a logger instance
logger = logging.getLogger()

# Log a message using the custom level and method
logger.verbose("This is a verbose message")
