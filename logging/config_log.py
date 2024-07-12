from logging import *
basicConfig(filename="logfile.log",level=DEBUG, filemode='w') #default append mode :level=DEBUG shows from base level debug to high levels else shows only high levels from
 
debug("this is Debug in w mode")
info("this is info")
warning("this is the warning message")
error("this is errror")
critical("this is critical")

