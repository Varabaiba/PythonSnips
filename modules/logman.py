import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Stream handler definition
c_handler = logging.StreamHandler()
c_format = logging.Formatter('T:%(asctime)s - M:%(module)s - LN:%(lineno)4d - LVL:%(levelname)s - %(message)s', 
                             datefmt='%d/%m/%y %H:%M:%S')
c_handler.setFormatter(c_format)
c_handler.setLevel(logging.DEBUG)
# Master handler enabler
logger.addHandler(c_handler)


# File handler definition
f_handler = logging.FileHandler('file.log')
f_format = logging.Formatter('T:%(asctime)s - M:%(module)s - LN:%(lineno)4d - LVL:%(levelname)s - %(message)s', 
                             datefmt='%d/%m/%y %H:%M:%S')
f_handler.setFormatter(f_format)
f_handler.setLevel(logging.DEBUG)
# Master handler enabler
logger.addHandler(f_handler)

# Regular Logger Calls
# logger.debug('This is a debug message')
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# logger.critical('This is a critical message')
# logger.log(15, "This is a manual message" )
# logger.log(): Manually emits a logging message with a specific log level.
# logger.exception(): Creates an ERROR level logging message wrapping the current exception stack frame.
