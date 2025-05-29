import logging
import os
from datetime import datetime
from pythonjsonlogger import jsonlogger

class CustomLogger:
    _instance = None
    _initialized = False

    def __new__(cls, name="selenium_test"):
        if cls._instance is None:
            cls._instance = super(CustomLogger, cls).__new__(cls)
        return cls._instance

    def __init__(self, name="selenium_test"):
        if not self._initialized:
            self.logger = logging.getLogger(name)
            self.logger.setLevel(logging.INFO)
            
            # Remove any existing handlers to prevent duplicates
            if self.logger.handlers:
                self.logger.handlers.clear()
            
            # Create logs directory if it doesn't exist
            if not os.path.exists("logs"):
                os.makedirs("logs")
                
            # File handler for JSON logs
            log_file = f"logs/test_run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(logging.INFO)
            
            # Console handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            
            # Create formatters
            json_formatter = jsonlogger.JsonFormatter(
                '%(asctime)s %(name)s %(levelname)s %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            console_formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            
            # Set formatters
            file_handler.setFormatter(json_formatter)
            console_handler.setFormatter(console_formatter)
            
            # Add handlers
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)
            
            self._initialized = True
    
    def info(self, message):
        self.logger.info(message)
    
    def error(self, message):
        self.logger.error(message)
    
    def warning(self, message):
        self.logger.warning(message)
    
    def debug(self, message):
        self.logger.debug(message) 