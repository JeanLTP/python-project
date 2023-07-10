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

        home_page.acess_cart()

        # Click checkout
        cart_page.checkout()

        # Completing forms to checkout
        cart_page.checkout_inf("Teste", "checkout", "99999999")
