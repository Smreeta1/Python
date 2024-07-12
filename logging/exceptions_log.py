import logging


# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
					filemode='w',  filename='exception_log.log')
logger = logging.getLogger(__name__)

def divide_numbers(x, y):
    try:
        result = x / y
        logger.info("Division result: %s", result)
    except ZeroDivisionError as ve:
        logger.error("Attempted to divide by zero: %s", str(ve))
    except Exception as e:
        logger.exception("An unexpected error occurred: %s", str(e))

def main():
    try:
        divide_numbers(10, 0)  #Will raise a ZeroDivisionError
    except ValueError as ve:
        logger.error("ValueError occurred: %s", str(ve))
    except Exception as e:
        logger.exception("An unexpected error occurred: %s", str(e))

if __name__ == "__main__":
    main()
