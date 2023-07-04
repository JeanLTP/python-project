import pytest
from conftest import setup_teardown
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.addItems
class TestAddItems:
    def test_add_items(self):
        home_page = HomePage()
        login_page = LoginPage()
        login_page.login("standard_user", "secret_sauce")
        cart_page = CartPage()

        product1 = "Sauce Labs Backpack"
        product2 = "Sauce Labs Bike Light"

        # Add items
        home_page.add_item_cart(product1)

        # Verifying if backpack was add to cart
        home_page.acess_cart()
        cart_page.verify_item_cart(product1)

        # Click to return shopping
        cart_page.return_shopping()

        # Add more one item to cart
        home_page.add_item_cart(product2)

        # Verifying cart
        home_page.acess_cart()
        cart_page.verify_item_cart(product1)
        cart_page.verify_item_cart(product2)
