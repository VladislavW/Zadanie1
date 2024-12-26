from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    # Описание перехода на страницу авторизации
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://10.10.215.5/"

    # Поиск элемента по локатору
    def find_element(self, locator,time = 10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                     message = f"Не найти элементы по локатору {locator}")
    # Переход на страницу авторизации
    def go_to_site(self):
        return self.driver.get(self.base_url)