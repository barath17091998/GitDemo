import logging


class BaseClass:

    def getLogger(self):

        logger = logging.getLogger(__name__)  # __name__ ==> prints the python file name
        fileHandler = logging.FileHandler('logfile.log')
        # To print the time and date in the log
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)  # INFO level - takes the log from INFO to CRITICAL
        return logger



