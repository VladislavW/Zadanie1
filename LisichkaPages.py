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

# Локаторы на главной странице
class LisichkaLocatorsMainPage:
    LOCATOR_LISICHKA_MAIN_PAGE_USERS = (By.ID, "menuUsersOpener")
    LOCATOR_LISICHKA_MAIN_PAGE_USERS_ADD = (By.ID, "menuUserAdd")

# Локаторы на странице списка пользователей
class LisichkaLocatorsUsersList:
    LOCATOR_LISICHKA_MAIN_PAGE_ADD_USER = (By.ID, "addUser")

# Локаторы на странице добавления пользователя
class LisichkaLocatorsAddUser:
    LOCATOR_LISICHKA_ADD_USER_EMAIL_FIELD = (By.ID, "dataEmail")
    LOCATOR_LISICHKA_ADD_USER_PASSWORD_FIELD = (By.ID, "dataPassword")
    LOCATOR_LISICHKA_ADD_USER_NAME_FIELD = (By.ID, "dataName")
    LOCATOR_LISICHKA_ADD_USER_GENDER_DROP_LIST = (By.ID, "dataGender")
    LOCATOR_LISICHKA_ADD_USER_GENDER_DROP_LIST_MALE = (By.XPATH, "//select[@id='dataGender']/option[1]")
    LOCATOR_LISICHKA_ADD_USER_GENDER_DROP_LIST_FEMALE = (By.XPATH, "//select[@id='dataGender']/option[2]")
    LOCATOR_LISICHKA_ADD_USER_RADIOBUTTON_11 = (By.ID, "dataSelect11")
    LOCATOR_LISICHKA_ADD_USER_RADIOBUTTON_12 = (By.ID, "dataSelect12")
    LOCATOR_LISICHKA_ADD_USER_CHECKBOX_21 = (By.ID, "dataSelect21")
    LOCATOR_LISICHKA_ADD_USER_CHECKBOX_22 = (By.ID, "dataSelect22")
    LOCATOR_LISICHKA_ADD_USER_CHECKBOX_23 = (By.ID, "dataSelect23")
    LOCATOR_LISICHKA_ADD_USER_BUTTON_ADD = (By.ID, "dataSend")
    LOCATOR_LISICHKA_ADD_USER_DIALOG_MESSAGE = (By.CLASS_NAME, "uk-modal-body")
    LOCATOR_LISICHKA_ADD_USER_DIALOG_BUTTON = (By.CLASS_NAME, "uk-modal-close")
    LOCATOR_LISICHKA_ADD_USER_MAIL_FORMAT_ERROR_MESSAGE = (By.ID, "emailFormatError")
    LOCATOR_LISICHKA_ADD_USER_NULL_PASSWORD_ERROR_MESSAGE = (By.ID, "blankPasswordError")
    LOCATOR_LISICHKA_ADD_USER_NULL_NAME_ERROR_MESSAGE = (By.ID, "blankNameError")

class DataForAuthorization:
    email = "test@protei.ru"
    password = "test"


class Autorization(BasePage):

    # Нажатие поле ввода "E-mail"
    def enter_email(self, email):
        search_email_field = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
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
        search_error_field = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            LisichkaLocatorsAutorization.LOCATOR_LISICHKA_AUTORIZATION_ENTER_ERROR_FIELD)).text
        #search_error_field = self.find_element(LisichkaLocatorsAutorization.LOCATOR_LISICHKA_AUTORIZATION_ENTER_ERROR_FIELD).text
        return search_error_field

   # Поиск текста всплывающего окна "Неверный E-Mail или пароль"
    def find_error_message2(self):
        search_error_field2 = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            LisichkaLocatorsAutorization.LOCATOR_LISICHKA_AUTORIZATION_ENTER_ERROR_FIELD2)).text
        #search_error_field2 = self.find_element(LisichkaLocatorsAutorization.LOCATOR_LISICHKA_AUTORIZATION_ENTER_ERROR_FIELD2).text
        return search_error_field2

    # Поиск текста "Добро пожаловать" после авторизации
    def find_greetings(self):
        search_main_page = WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(
            LisichkaLocatorsAutorization.LOCATOR_LISICHKA_AUTORIZATION_MAIN_PAGE_TEXT)).text
        #search_main_page = self.find_element(LisichkaLocatorsAutorization.LOCATOR_LISICHKA_AUTORIZATION_MAIN_PAGE_TEXT).text
        return search_main_page



class add_user(BasePage):

    # Ввод Email "test@protei.ru"
    def enter_email_test_protei_ru(self, email):
        search_email_field = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            LisichkaLocatorsAutorization.LOCATOR_LISICHKA_AUTORIZATION_EMAIL_FIELD))
            # search_email_field = self.find_element(LisichkaLocatorsAutorization.LOCATOR_LISICHKA_AUTORIZATION_EMAIL_FIELD)
        search_email_field.send_keys(email)
        return search_email_field

    # Ввод Password "test"
    def enter_password_test(self, password):
        search_password_field = self.find_element(
            LisichkaLocatorsAutorization.LOCATOR_LISICHKA_AUTORIZATION_PASSWORD_FIELD)
        search_password_field.send_keys(password)
        return search_password_field

    def press_autorization_button1(self):
        search_button_field = self.find_element(LisichkaLocatorsAutorization.LOCATOR_LISICHKA_AUTORIZATION_ENTER_BUTTON_FIELD)
        return search_button_field.click()

    # Вызов всплывающего окна
    def to_users_button(self):
        search_button_users = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            LisichkaLocatorsMainPage.LOCATOR_LISICHKA_MAIN_PAGE_USERS))
        #search_button_users = self.find_element(LisichkaLocatorsMainPage.LOCATOR_LISICHKA_MAIN_PAGE_USERS)
        return search_button_users.click()

    # Переход на страницу добавления пользователя
    def to_user_add(self):
        search_button_add_users = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            LisichkaLocatorsMainPage.LOCATOR_LISICHKA_MAIN_PAGE_USERS_ADD))
        #search_button_users = self.find_element(LisichkaLocatorsMainPage.LOCATOR_LISICHKA_MAIN_PAGE_USERS)
        return search_button_add_users.click()

    # Переход на страницу добавления пользователей
    def to_add_users(self):
        search_button_add_user = self.find_element(LisichkaLocatorsUsersList.LOCATOR_LISICHKA_MAIN_PAGE_ADD_USER)
        return search_button_add_user.click()

    # Ввод Email на добавлении пользователя
    def enter_email_in_add_user(self, email):
        search_email_field_in_add_user = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            LisichkaLocatorsAddUser.LOCATOR_LISICHKA_ADD_USER_EMAIL_FIELD))
        search_email_field_in_add_user.send_keys(email)
        return search_email_field_in_add_user

    # Ввод пароля на добавлении пользователя
    def enter_password_in_add_user(self, password):
        search_password_field_in_add_user = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            LisichkaLocatorsAddUser.LOCATOR_LISICHKA_ADD_USER_PASSWORD_FIELD))
        search_password_field_in_add_user.send_keys(password)
        return search_password_field_in_add_user

    # Ввод имени на добавлении пользователя
    def enter_name_in_add_user(self, name):
        search_name_field_in_add_user = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            LisichkaLocatorsAddUser.LOCATOR_LISICHKA_ADD_USER_NAME_FIELD))
        search_name_field_in_add_user.send_keys(name)
        return search_name_field_in_add_user

    # Нажатие дропдауна на выбор гендера
    def click_gender_in_add_user(self):
        click_dropdown_in_add_user = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            LisichkaLocatorsAddUser.LOCATOR_LISICHKA_ADD_USER_GENDER_DROP_LIST))
        return click_dropdown_in_add_user.click()

    # Выбор мужского гендера
    def click_male_gender_in_add_user(self):
        click_to_male_in_add_user = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
                LisichkaLocatorsAddUser.LOCATOR_LISICHKA_ADD_USER_GENDER_DROP_LIST_MALE))
        return click_to_male_in_add_user.click()

    # Выбор женского гендера
    def click_female_gender_in_add_user(self):
        click_to_female_in_add_user = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
                LisichkaLocatorsAddUser.LOCATOR_LISICHKA_ADD_USER_GENDER_DROP_LIST_FEMALE))
        return click_to_female_in_add_user.click()

    # Нажатие кнопки вариант 1.1
    def click_radiobutton11_in_add_user(self):
        click_to_radiobutton11_in_add_user = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
                LisichkaLocatorsAddUser.LOCATOR_LISICHKA_ADD_USER_RADIOBUTTON_11))
        return click_to_radiobutton11_in_add_user.click()

    # Нажатие кнопки вариант 1.2
    def click_radiobutton12_in_add_user(self):
        click_to_radiobutton12_in_add_user = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
                LisichkaLocatorsAddUser.LOCATOR_LISICHKA_ADD_USER_RADIOBUTTON_12))
        return click_to_radiobutton12_in_add_user.click()

    # Нажатие чекбокса вариант 2.1
    def click_checkbox21_in_add_user(self):
        click_to_checkbox21_in_add_user = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
                LisichkaLocatorsAddUser.LOCATOR_LISICHKA_ADD_USER_CHECKBOX_21))
        return click_to_checkbox21_in_add_user.click()

    # Нажатие чекбокса вариант 2.2
    def click_checkbox22_in_add_user(self):
        click_to_checkbox22_in_add_user = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
                LisichkaLocatorsAddUser.LOCATOR_LISICHKA_ADD_USER_CHECKBOX_22))
        return click_to_checkbox22_in_add_user.click()

    # Нажатие чекбокса вариант 2.3
    def click_checkbox23_in_add_user(self):
        click_to_checkbox23_in_add_user = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
                LisichkaLocatorsAddUser.LOCATOR_LISICHKA_ADD_USER_CHECKBOX_23))
        return click_to_checkbox23_in_add_user.click()

    # Нажатие кнопки Добавления
    def click_add_button_in_add_user(self):
        click_to_add_in_add_user = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
                LisichkaLocatorsAddUser.LOCATOR_LISICHKA_ADD_USER_BUTTON_ADD))
        return click_to_add_in_add_user.click()

    # Считывание сообщения об ошибке при неправильном формате E-Mail
    def search_email_format_error_in_add_user(self):
        search_to_email_format_error_in_add_user = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
                LisichkaLocatorsAddUser.LOCATOR_LISICHKA_ADD_USER_MAIL_FORMAT_ERROR_MESSAGE)).text
        return search_to_email_format_error_in_add_user

    # Считывание сообщения об ошибке при пустом вводе пароля
    def search_null_password_error_in_add_user(self):
        search_to_null_password_error_in_add_user = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
                LisichkaLocatorsAddUser.LOCATOR_LISICHKA_ADD_USER_NULL_PASSWORD_ERROR_MESSAGE)).text
        return search_to_null_password_error_in_add_user

    # Считывание сообщения об ошибке при пустом вводе имени
    def search_null_name_error_in_add_user(self):
        search_to_null_name_error_in_add_user = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
                LisichkaLocatorsAddUser.LOCATOR_LISICHKA_ADD_USER_NULL_NAME_ERROR_MESSAGE)).text
        return search_to_null_name_error_in_add_user

    # Считывание сообщения о успехе добавления "Данные добавлены."
    def search_user_added_in_add_user(self):
        search_to_user_added_in_add_user = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
                LisichkaLocatorsAddUser.LOCATOR_LISICHKA_ADD_USER_DIALOG_MESSAGE)).text
        return search_to_user_added_in_add_user

    # Нажатие кнопки "ОК" в сообщении о успехе добавления
    def click_ok_in_dialog_message_in_add_user(self):
        click_to_ok_in_dialog_message_user = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
                LisichkaLocatorsAddUser.LOCATOR_LISICHKA_ADD_USER_DIALOG_BUTTON))
        return click_to_ok_in_dialog_message_user.click()




