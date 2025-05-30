# Selenium Pytest Project

This project contains automated tests for the email batch expansion and minimization functionality using Selenium and pytest.

## Project Structure

```
V6/
│
├── tests/
│   ├── test_email_batch.py        # Actual test cases using pytest
│   ├── conftest.py                # Fixtures like driver setup
│
├── pages/
│   ├── login_page.py              # Page Object for login
│   ├── dashboard_page.py          # Page Object for batch expansion
│
├── config/
│   ├── config.yaml                # Config file for URLs, credentials, etc.
│
├── utils/
│   ├── helpers.py                 # Utility functions (e.g., read config)
│
├── requirements.txt               # Python dependencies
├── pytest.ini                     # Pytest config file
└── README.md                      # Documentation
```

## Setup

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the tests:
   ```
   pytest
   ```

3. Run a specific file
   ```
   pytest tests/test_1login.py -v --html=reports/report.html --self-contained-html
   ```

4. Run all file
   ```
   pytest -v --html=reports/report.html --self-contained-html
   ```

## Notes

- The `driver` fixture is defined in `tests/conftest.py` to ensure pytest can discover it.
- Configuration values (URLs, credentials) are stored in `config/config.yaml`.
- Page Objects in `pages/` encapsulate UI interactions for better maintainability.