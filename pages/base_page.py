from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://b2c.passport.rt.ru/'
        self.lk_auth_url = 'https://lk.rt.ru/'

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time, 1).until(EC.presence_of_element_located(locator),
                                                         message=f'Невозможно найти элемент по локатору: {locator}')

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time, 1).until(EC.presence_of_all_elements_located(locator),
                                                         message=f"Невозможно найти элементы по локатору: {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def go_to_lk_auth_page(self, time=10):
        self.driver.get(self.lk_auth_url)
        return WebDriverWait(self.driver, time, 1).until(EC.url_contains('auth'),
                                                         "Страница авторизации не загрузилась")