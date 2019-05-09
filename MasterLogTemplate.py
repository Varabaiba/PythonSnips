import logging

logger = logging.getLogger(__name__)
#Magic necessary to set minimum logging level for all handlers
logger.setLevel(logging.DEBUG)
#do not use this as advised sowhere - logging.basicConfig(level=logging.DEBUG)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')


# Create formatters and add it to handlers
c_format = logging.Formatter('T:%(asctime)s - M:%(module)s - LN:%(lineno)4d - LVL:%(levelname)s - %(message)s',
           datefmt='%d/%m/%y %H:%M:%S')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%m-%y %H:%M:%S')
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
