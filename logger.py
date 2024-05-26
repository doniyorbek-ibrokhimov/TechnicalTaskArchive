import logging


# Configuring logging with a basic configuration
logging.basicConfig(
    level=logging.INFO,  # Setting log level to INFO
    format='%(asctime)s - %(levelname)s - %(message)s',  # Formatting log messages
    handlers=[
        logging.StreamHandler()  # Adding a StreamHandler to log to console
    ]
)

# Creating a logger instance for the current module
logger = logging.getLogger(__name__)
