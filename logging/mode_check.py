import os
import logging
from pathlib import Path


os.environ['APP_ENV'] = 'production' 

#   Specify development or production mode 
ENVIRONMENT = os.getenv('APP_ENV', 'production')

print(f"Running in {ENVIRONMENT} mode")
 
'''     log_dir = '/s/Ankamala/Venv test/logging'
logfile_path = os.path.join(log_dir, 'mode_check.log')
-->Removing hardcoding
'''
#directory of current script
script_dir = Path(__file__).resolve().parent
log_dir = script_dir

if ENVIRONMENT == 'development':
    #Development mode:Print log messages to console
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')
else:
    #Production mode: Log messages to a file
    logfile_path = log_dir /'mode_check.log'

    try:
        print(f"Attempting to create log directory: {log_dir}")
        log_dir.mkdir(parents=True, exist_ok=True)
        print(f"Log directory created or already exists: {log_dir}")

        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            filename=logfile_path,
                            filemode='a')
        print(f"Log file will be at: {logfile_path}")
    except Exception as e:
        print(f"Failed to create log directory or configure logging: {e}")

# Eg. logging messages
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')




