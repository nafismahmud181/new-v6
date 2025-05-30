import pytest
from pages.login_page import LoginPage
from utils.helpers import read_config
from utils.logger import CustomLogger
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = CustomLogger()

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

def test_invalid_login(driver):
    logger.info("Starting invalid login test")
    try:
        login_page = LoginPage(driver)
        logger.info("Attempting to login with invalid credentials")
        
        # Try to login with invalid credentials
        with pytest.raises(Exception) as exc_info:
            login_page.login("invalid_user", "invalid_pass")
        
        # Verify the error message element is present
        error_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='alert-body']"))
        )
        assert error_message.is_displayed(), "Unable to log in with provided credentials."
        logger.info(f"Test passed: Invalid login error message found: {error_message.text}")
            
    except Exception as e:
        logger.error(f"Test failed with error: {str(e)}")
        raise

def test_empty_credentials(driver):
    logger.info("Starting empty credentials test")
    try:
        login_page = LoginPage(driver)
        logger.info("Attempting to login with empty credentials")
        with pytest.raises(Exception) as exc_info:
            login_page.login("", "")
        logger.info(f"Test passed: Empty credentials raised exception: {str(exc_info.value)}")
            
    except Exception as e:
        logger.error(f"Test failed with error: {str(e)}")
        raise

def test_valid_login(logged_in_driver):
    """Test to verify login was successful"""
    logger.info("Verifying login status")
    try:
        # The logged_in_driver fixture already handles the login and wait
        current_url = logged_in_driver.current_url
        logger.info(f"Current URL after login: {current_url}")
        assert current_url != "http://10.10.1.10/login", "Still on login page after login attempt"
        logger.info("Login verification successful")
        
    except Exception as e:
        logger.error(f"Login verification failed: {str(e)}")
        raise