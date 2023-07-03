import pytest
from selenium.webdriver.common.by import By
import conftest
from conftest import setup_teardown
from pages.login_page import LoginPage


# Login
@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestInvalidLogin:
    def test_invalid_login(self):
        message_error_login = "Epic sadface: Username and password do not match any user in this service"
        driver = conftest.driver
        login_page = LoginPage()
        login_page.login("standard_user", "secret_sauce123")
        login_page.verify_error_login()
        login_page.compare_text_error_login(message_error_login)
