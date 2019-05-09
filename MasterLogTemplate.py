#Thanks to RealPython: https://realpython.com/python-logging/
import logging

logger = logging.getLogger(__name__)
#logging.basicConfig(level=logging.DEBUG)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')


# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
c_handler.setLevel(logging.DEBUG)
f_handler.setLevel(logging.DEBUG)
logger.addHandler(c_handler)
logger.addHandler(f_handler)



logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
