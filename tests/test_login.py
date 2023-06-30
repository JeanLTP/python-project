import pytest
from selenium.webdriver.common.by import By
import conftest
from conftest import setup_teardown
from pages.login_page import LoginPage


# Login
@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestLogin:
    def test_login(self):
        driver = conftest.driver
        login_page = LoginPage()

        login_page.login("standard_user", "secret_sauce")
        # driver.find_element(By.ID, "user-name").send_keys("standard_user")
        # driver.find_element(By.ID, "password").send_keys("secret_sauce")
        # driver.find_element(By.ID, "login-button").click()
        assert driver.find_element(By.XPATH, "*//span[@class='title']").is_displayed()