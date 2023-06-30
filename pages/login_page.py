import conftest
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.user_name_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.btn_login = (By.ID, "login-button")

    def login(self, user, pwd):
        self.write(self.user_name_field, user)
        self.write(self.password_field, pwd)
        self.cli(self.btn_login)
