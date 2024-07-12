import logging

# Creating a custom logger
logger = logging.getLogger('web_app')

# Creating handlers
console_handler = logging.StreamHandler()  #StreamHandler for logging to the console
file_handler = logging.FileHandler('web_app.log')  # FileHandler for logging to a file
error_handler = logging.FileHandler('web_app_errors.log')  # Produce diff fileHandler for error logs

# Set levels for handlers
console_handler.setLevel(logging.INFO)  # Set console handler to log INFO and above
file_handler.setLevel(logging.DEBUG)  # Set file handler to log DEBUG and above
error_handler.setLevel(logging.ERROR)  # Set error handler to log ERROR and above

# Create formatters and add them to handlers
console_format = logging.Formatter('%(levelname)s: %(message)s')  # Simple format for console output
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # Detailed format for file output
error_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # Detailed format for error file output
console_handler.setFormatter(console_format)  # Apply format to console handler
file_handler.setFormatter(file_format)  # Apply format to file handler
error_handler.setFormatter(error_format)  # Apply format to error handler

# Add handlers to the logger
logger.addHandler(console_handler)  # Add console handler to logger
logger.addHandler(file_handler)  # Add file handler to logger
logger.addHandler(error_handler)  # Add error handler to logger

#logging levelset for the logger
logger.setLevel(logging.DEBUG)
  
# Log messages of diff levels
logger.debug('Debugging information, useful for diagnosing issues')
logger.info('Informational message, such as application start/stop')
logger.warning('Warning message, something unexpected but not critical')
logger.error('Error message, an issue that requires attention')
logger.critical('Critical message, a serious error indicating potential failure')

# Example of logging in a web_app
def authenticate_user(username):
    if username == 'admin':
        logger.info(f'User {username} authenticated successfully.')
    else:
        logger.warning(f'Failed authentication attempt for user {username}.')

def handle_request(request):
    try:
        #request handling
        logger.info(f'Handling request: {request}')
        if request == 'error':
            raise ValueError('Simulated error!')
    except Exception as e:
        logger.error(f'Error handling request {request}: {e}')

authenticate_user('admin')
authenticate_user('guest')
handle_request('home')
handle_request('error')
