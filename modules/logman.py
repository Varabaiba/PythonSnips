import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# Stream handler definition
cons_log = logging.StreamHandler()
c_format = logging.Formatter('T:%(asctime)s - M:%(module)s - LN:%(lineno)4d - LVL:%(levelname)s - %(message)s',
                             datefmt='%d/%m/%y %H:%M:%S')
cons_log.setFormatter(c_format)
cons_log.setLevel(logging.DEBUG)
# Master handler enabler
log.addHandler(cons_log)


# File handler definition
file_log = logging.FileHandler('debug.log')
f_format = logging.Formatter('T:%(asctime)s - M:%(module)s - LN:%(lineno)4d - LVL:%(levelname)s - %(message)s',
                             datefmt='%d/%m/%y %H:%M:%S')
file_log.setFormatter(f_format)
file_log.setLevel(logging.DEBUG)
# Master handler enabler
log.addHandler(file_log)

# Regular Logger Calls
# logger.debug('This is a debug message')
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# logger.critical('This is a critical message')
# logger.log(15, "This is a manual message" )
# logger.log(): Manually emits a logging message with a specific log level.
# logger.exception(): Creates an ERROR level logging message wrapping the current exception stack frame.
