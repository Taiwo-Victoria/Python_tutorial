import logging
'''
logging.basicConfig(level= logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')

import main

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
'''
#setting different log handlers
loggers = logging.getLogger(__name__)

#create handler

stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

#setting the level and format

stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

loggers.addHandler((stream_h))
loggers.addHandler(file_h)

loggers.warning('This is the warning message')
loggers.error('This is the error message')