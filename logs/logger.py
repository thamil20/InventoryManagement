import sys
import os
import logging

class Logger:
    def __init__(self, pathToLog):
        self.logger = logging.getLogger("Logger")
        try:
            logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                level=logging.DEBUG,
                                datefmt='%d/%m/%Y %H:%M:%S',
                                filename=pathToLog,
                                filemode='a')

        except FileNotFoundError:
            with open(f"./{pathToLog}", 'w') as file:
                pass


    def infoLog(self, message) -> None:
        self.logger.setLevel(logging.INFO)
        self.logger.info(message)

    def debugLog(self, message) -> None:
        self.logger.setLevel(logging.DEBUG)
        self.logger.debug(message)

    def errorLog(self, message):
        self.logger.setLevel(logging.ERROR)
        self.logger.error(message)

    def criticalLog(self, message):
        self.logger.setLevel(logging.CRITICAL)
        self.logger.critical(message)

    def warningLog(self, message):
        self.logger.setLevel(logging.WARNING)
        self.logger.warning(message)

    def callAllForTesting(self, message) -> None:
        self.infoLog(message)
        self.debugLog(message)
        self.errorLog(message)
        self.criticalLog(message)
        self.warningLog(message)


def main():
    run = Logger("log1.log")
    run.callAllForTesting("Testing")

if __name__ == '__main__':
    main()