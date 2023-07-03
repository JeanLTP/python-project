import conftest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys

class BasePage:
    def __init__(self):
        self.driver = conftest.driver

    def fe(self, locator):
            return self.driver.find_element(*locator)

    def fes(self, locator):
            return self.driver.find_elements(*locator)

    def write(self, locator, text):
        self.fe(locator).send_keys(text)

    def cli(self, locator):
        self.fe(locator).click()

    def verify_el_exist(self, locator):
        assert self.fe(locator).is_displayed(), f"Element '{locator}' is not displayed"

    def find_text(self, locator):
        self.wait_el(locator)
        return self.fe(locator).text

    def wait_el(self, locator, timeout=3):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(*locator))

    def double_cli(self, locator):
        element = self.wait_el(locator)
        ActionChains(self.driver).double_click(element).perform()

    def right_click(self, locator):
        element = self.wait_el(locator)
        ActionChains(self.driver).context_click(element).perform()

    def press_key(self, locator, key):
        el = self.fe(locator)
        if key == "ENTER":
            el.send_keys(Keys.ENTER)
        elif key == "SPACE":
            el.send_keys(Keys.SPACE)
        elif key == "PGDOWN":
            el.send_keys(Keys.PAGE_DOWN)
