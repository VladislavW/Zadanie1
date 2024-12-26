from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

# Локаторы на странице авторизации и главной странице
class LisichkaLocatorsAutorization:
    LOCATOR_LISICHKA_AUTORIZATION_EMAIL_FIELD = (By.ID, "loginEmail")
    LOCATOR_LISICHKA_AUTORIZATION_PASSWORD_FIELD = (By.ID, "loginPassword")
    LOCATOR_LISICHKA_AUTORIZATION_ENTER_BUTTON_FIELD = (By.ID, "authButton")
    LOCATOR_LISICHKA_AUTORIZATION_ENTER_ERROR_FIELD = (By.ID, "emailFormatError") # Для сообщения о неверном E-Mail
    LOCATOR_LISICHKA_AUTORIZATION_ENTER_ERROR_FIELD2 = (By.ID, "KEKEKEKEKEKKEKE") # Для сообщения о неверном E-Mail или пароле
    LOCATOR_LISICHKA_AUTORIZATION_MAIN_PAGE_TEXT = (By.CSS_SELECTOR, "h3")


class Autorization(BasePage):

    # Нажатие поле ввода "E-mail"
    def enter_email(self, email):
        search_email_field = WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(
            LisichkaLocatorsAutorization.LOCATOR_LISICHKA_AUTORIZATION_EMAIL_FIELD))
        #search_email_field = self.find_element(LisichkaLocatorsAutorization.LOCATOR_LISICHKA_AUTORIZATION_EMAIL_FIELD)
        search_email_field.send_keys(email)
        return search_email_field


    # Нажатие поле ввода "Пароль"
    def enter_password(self, password):
        search_password_field = self.find_element(LisichkaLocatorsAutorization.LOCATOR_LISICHKA_AUTORIZATION_PASSWORD_FIELD)
        search_password_field.send_keys(password)
        return search_password_field

    # Нажатие кнопки "ВХОД"
    def press_button(self):
        search_button_field = self.find_element(LisichkaLocatorsAutorization.LOCATOR_LISICHKA_AUTORIZATION_ENTER_BUTTON_FIELD)
        return search_button_field.click()

    # Поиск текста всплывающего окна "Неверный формат E-mail"
    def find_error_message(self):
        search_error_field = WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(
            LisichkaLocatorsAutorization.LOCATOR_LISICHKA_AUTORIZATION_ENTER_ERROR_FIELD)).text
        #search_error_field = self.find_element(LisichkaLocatorsAutorization.LOCATOR_LISICHKA_AUTORIZATION_ENTER_ERROR_FIELD).text
        return search_error_field

   # Поиск текста всплывающего окна "Неверный E-Mail или пароль"
    def find_error_message2(self):
        search_error_field2 = WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(
            LisichkaLocatorsAutorization.LOCATOR_LISICHKA_AUTORIZATION_ENTER_ERROR_FIELD2)).text
        #search_error_field2 = self.find_element(LisichkaLocatorsAutorization.LOCATOR_LISICHKA_AUTORIZATION_ENTER_ERROR_FIELD2).text
        return search_error_field2

    # Поиск текста "Добро пожаловать" после авторизации
    def find_greetings(self):
        search_main_page = WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(
            LisichkaLocatorsAutorization.LOCATOR_LISICHKA_AUTORIZATION_MAIN_PAGE_TEXT)).text
        #search_main_page = self.find_element(LisichkaLocatorsAutorization.LOCATOR_LISICHKA_AUTORIZATION_MAIN_PAGE_TEXT).text
        return search_main_page
