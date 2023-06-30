import pytest
from selenium.webdriver.common.by import By
import conftest
from conftest import setup_teardown
from pages.login_page import LoginPage


# Login
@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.addItems
class TestAddItems:
    def test_add_items(self):
        driver = conftest.driver

        login_page = LoginPage()
        login_page.login("standard_user", "secret_sauce")

        # Add items
        driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").click()
        driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()

        # Verifing if backpack was add to cart
        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
        assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

        # Click to return home
        driver.find_element(By.ID, "continue-shopping").click()

        # Add more one item to cart
        driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").click()
        driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()

        # Verifing cart
        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
        assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
        assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").is_displayed()
