from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.item_add = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.btn_return = (By.ID, "continue-shopping")
        self.btn_checkout = (By.ID, "checkout")
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.zip = (By.ID, "postal-code")
        self.btn_continue = (By.ID, "continue")
        self.btn_finish = (By.ID, "finish")
        self.text_checkout = (By.XPATH, "//h2 [@class='complete-header']")


    def verify_item_cart(self, name_item):
        item = (self.item_add[0], self.item_add[1].format(name_item))
        self.verify_el_exist(item)

    def return_shopping(self):
        self.cli(self.btn_return)

    def checkout(self):
        self.cli(self.btn_checkout)

    def checkout_inf(self, firstname, lastname, zipcode):
        self.write(self.first_name, firstname)
        self.write(self.last_name, lastname)
        self.write(self.zip, zipcode)
        self.cli(self.btn_continue)
        self.cli(self.btn_finish)
        self.verify_el_exist(self.text_checkout)
