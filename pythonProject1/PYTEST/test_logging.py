import logging

def test_logging():
    logger = logging.getLogger(__name__)    #__name__ ==> prints the python file name
    fileHandler = logging.FileHandler('logfile.log')
    # To print the time and date in the log
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)         #filehandler object
    logger.setLevel(logging.INFO)           # INFO level - takes the log from INFO to CRITICAL
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Something is in warning mode")
    logger.error("A major error")
    logger.critical("Critical issue")
