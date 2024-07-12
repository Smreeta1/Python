from logging import *  # Importing all functions and classes from the logging module

# Define the logging format
log_format = '%(asctime)s %(message)s'

# Configure the basic settings for logging
basicConfig(
    filename="logfile.log",  # Set the log file name
    level=DEBUG,             # Set the logging level to DEBUG (shows all levels from DEBUG to CRITICAL)
    format=log_format,       # Apply the log format defined above
               # Set the file mode to 'w' (write mode), which overwrites the log file each time:In default=append
)

# Log messages of all levels
debug("this is Debug in w mode")   
info("this is info")               
warning("this is the warning message")  
error("this is error")             
critical("this is critical")      
