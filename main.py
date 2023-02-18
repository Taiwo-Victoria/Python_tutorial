# logging on own(instead of root) module
import logging

logger = logging.getLogger(__name__) # create logger on module name
logger.info('Hello from Logging_')