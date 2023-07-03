import pytest
from conftest import setup_teardown
from pages.home_page import HomePage
from pages.login_page import LoginPage


# Login
@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestLogin:
    def test_login(self):
        # Instancia os objetos a serem usados
        login_page = LoginPage()
        home_page = HomePage()

        # Efetua login
        login_page.login("standard_user", "secret_sauce")

        # Verifica se login foi realizado com sucesso
        home_page.verify_login()

        # assert driver.find_element(By.XPATH, "*//span[@class='title']").is_displayed()
