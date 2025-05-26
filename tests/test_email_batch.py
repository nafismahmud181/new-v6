import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.helpers import read_config

@pytest.mark.parametrize("batch_number", ["20250526.00003"])  # Add more batch numbers as needed
def test_email_batch_expand_and_minimize(driver, batch_number):
    config = read_config()
    login_page = LoginPage(driver)
    login_page.login(config['credentials']['username'], config['credentials']['password'])
    dashboard_page = DashboardPage(driver)
    dashboard_page.expand_batch(batch_number)
    dashboard_page.minimize_batch(batch_number) 