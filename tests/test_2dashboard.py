import pytest
from pages.dashboard_page import DashboardPage
from utils.logger import CustomLogger

logger = CustomLogger()

@pytest.mark.usefixtures("logged_in_driver")
class TestDashboard:
    """Dashboard test suite - requires successful login"""
    
    @pytest.fixture(autouse=True)
    def setup(self, logged_in_driver):
        """Setup for each test"""
        self.driver = logged_in_driver
        self.dashboard_page = DashboardPage(self.driver)
    
    @pytest.mark.parametrize("batch_number", ["20250526.00003", "20250526.00002", "20250524.00002"])
    def test_batch_expand_and_minimize(self, batch_number):
        logger.info(f"Starting test for batch number: {batch_number}")
        try:
            logger.info(f"Attempting to expand batch: {batch_number}")
            self.dashboard_page.expand_batch(batch_number)
            logger.info("Batch expanded successfully")
            
            logger.info(f"Attempting to minimize batch: {batch_number}")
            self.dashboard_page.minimize_batch(batch_number)
            logger.info("Batch minimized successfully")
            
        except Exception as e:
            logger.error(f"Test failed with error: {str(e)}")
            raise

    def test_invalid_batch_number(self):
        logger.info("Starting test for invalid batch number")
        try:
            invalid_batch = "invalid_batch_number"
            logger.info(f"Attempting to expand invalid batch: {invalid_batch}")
            try:
                self.dashboard_page.expand_batch(invalid_batch)
                pytest.fail("Should have failed with invalid batch number")
            except Exception as e:
                logger.info("Test passed: Invalid batch number handled correctly")
                return
            
        except Exception as e:
            logger.error(f"Test failed with error: {str(e)}")
            raise

    # def test_batch_search(self):
    #     logger.info("Starting test for batch search functionality")
    #     try:
    #         search_term = "20250526"
    #         logger.info(f"Attempting to search for batch: {search_term}")
    #         results = self.dashboard_page.search_batch(search_term)
    #         logger.info(f"Search returned {len(results)} results")
    #         assert len(results) > 0, "Search should return at least one result"
    #         logger.info("Search functionality test passed")
            
    #     except Exception as e:
    #         logger.error(f"Test failed with error: {str(e)}")
    #         raise 

    