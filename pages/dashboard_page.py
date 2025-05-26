from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    def expand_batch(self, batch_number):
        xpath_expansion = f"//div[@data-id='email-batch {batch_number} action view-details']"
        expand_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_expansion))
        )
        expand_button.click()
        time.sleep(2)

    def minimize_batch(self, batch_number):
        xpath_expansion = f"//div[@data-id='email-batch {batch_number} action view-details']"
        expand_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_expansion))
        )
        expand_button.click()
        time.sleep(2) 