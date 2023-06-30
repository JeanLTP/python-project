import conftest


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
