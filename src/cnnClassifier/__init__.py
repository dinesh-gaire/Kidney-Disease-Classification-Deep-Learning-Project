# We can create a seperate file logger.py for this logging functionality
# we have to use logging functionality in every file so for easy importing we are writing code here

import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath), #to get logging file
        logging.StreamHandler(sys.stdout)   #to pring logs in terminal
    ]
)

logger = logging.getLogger("cnnClassifierLogger")