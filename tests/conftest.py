import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.helpers import read_config
from utils.logger import CustomLogger

logger = CustomLogger()

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def logged_in_driver(driver):
    """Module-wide fixture to handle login once for all tests"""
    logger.info("Starting login process")
    try:
        config = read_config()
        logger.info("Configuration loaded successfully")
        
        login_page = LoginPage(driver)
        logger.info("Attempting to login with valid credentials")
        login_page.login(config['credentials']['username'], config['credentials']['password'])
        logger.info("Login successful")
        
        return driver
    except Exception as e:
        logger.error(f"Login failed with error: {str(e)}")
        raise 