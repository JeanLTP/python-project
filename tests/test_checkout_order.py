import random
import time

import pytest
from selenium.webdriver.common.by import By

import conftest
from conftest import setup_teardown
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.addItems
class TestCheckoutOrder:
    def test_checkout_order(self):
        home_page = HomePage()
        login_page = LoginPage()
        login_page.login("standard_user", "secret_sauce")
        cart_page = CartPage()
        driver = conftest.driver

        # Add random item
        home_page.random_item()

        # feito sem usar o page obejcts
        # items = driver.find_elements(By.XPATH, "//button[@class='btn btn_primary btn_small btn_inventory']")
        # if items:
        #     random_element = random.choice(items)
        #     random_element.click()
        #     time.sleep(2)
        # else:
        #     print("Nenhum elemento encontrado.")


        # Verifying if backpack was add to cart
        home_page.acess_cart()

        # cart_page.verify_item_cart(product1)
