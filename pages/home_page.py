from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.title_page = (By.XPATH, "*//span[@class='title']")
        self.item_add = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.btn_cart_add = (By.XPATH, "//*[text()='Add to cart']")
        self.cart_icon = (By.XPATH, "//*[@class='shopping_cart_link']")
        # driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
        # assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

    def verify_login(self):
        self.verify_el_exis(self.title_page)

    def add_item_cart(self, item_name):
        item = (self.item_add[0], self.item_add[1].format(item_name))
        self.cli(item)
        self.cli(self.btn_cart_add)

    def acess_cart(self):
        self.cli(self.cart_icon)
