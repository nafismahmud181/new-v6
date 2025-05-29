from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.get("http://10.10.1.10/login")
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='login-username']"))
        )
        username_field.send_keys(username)
        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='login-password']"))
        )
        password_field.send_keys(password)
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Sign in']"))
        )
        login_button.click()
        
        # Wait for URL to change from login page
        try:
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.current_url != "http://10.10.1.10/login"
            )
        except TimeoutException:
            # If URL doesn't change, check for error message
            try:
                error_message = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'alert-danger')]"))
                )
                raise Exception(f"Login failed: {error_message.text}")
            except TimeoutException:
                raise Exception("Login failed: No redirect and no error message found") 