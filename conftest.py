from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from LisichkaPages import add_user, DataForAuthorization


@pytest.fixture(scope = "session")
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

@pytest.fixture(scope = "function")
def GO_TO_ADD_USERS(browser):
    lisichka_go_to_add_user_page = add_user(browser)
    lisichka_go_to_add_user_page.go_to_site()
    lisichka_go_to_add_user_page.enter_email_test_protei_ru(DataForAuthorization.email)
    lisichka_go_to_add_user_page.enter_password_test(DataForAuthorization.password)
    lisichka_go_to_add_user_page.press_autorization_button1()
    lisichka_go_to_add_user_page.to_users_button()
    #lisichka_go_to_add_user_page.to_add_users()
    lisichka_go_to_add_user_page.to_user_add()
    lisichka_add_user = lisichka_go_to_add_user_page
    return lisichka_add_user

