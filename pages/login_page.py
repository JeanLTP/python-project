import conftest
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.user_name_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.btn_login = (By.ID, "login-button")
        self.error_login = (By.XPATH, "//div[@class='error-message-container error']")

    def login(self, user, pwd):
        self.write(self.user_name_field, user)
        self.write(self.password_field, pwd)
        self.cli(self.btn_login)

    def verify_error_login(self):
        self.verify_el_exist(self.error_login)

    def compare_text_error_login(self, expected_text):
        found_text = self.find_text(self.error_login)
        assert found_text == expected_text, f"O texto encontrado foi '{found_text}' mas era esperado o texto '{expected_text}'"
