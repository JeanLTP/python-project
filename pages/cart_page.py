from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.item_add = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.btn_return = (By.ID, "continue-shopping")

    def verify_item_cart(self, name_item):
        item = (self.item_add[0], self.item_add[1].format(name_item))
        self.verify_el_exist(item)

    def return_shopping(self):
        self.cli(self.btn_return)
