from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys

def main():
    try:
        logging.info("Starting the main function")
        a=1/0
    except Exception as e:
        logging.info("Exception occured in main function")
        raise CustomException(e,sys)
if __name__=="__main__":
    main()