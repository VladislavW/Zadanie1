from LisichkaPages import Autorization

# Тестирование авторизации
def test_auth_id1(browser):
    lisichka_auth_page = Autorization(browser)
    lisichka_auth_page.go_to_site()
    lisichka_auth_page.enter_email("test@protei.ru")
    lisichka_auth_page.enter_password("test")
    lisichka_auth_page.press_button()
    assert lisichka_auth_page.find_greetings() == "Добро пожаловать!"

def test_auth_id2(browser):
    lisichka_auth_page = Autorization(browser)
    lisichka_auth_page.go_to_site()
    lisichka_auth_page.enter_email("test@protei.ru")
    lisichka_auth_page.enter_password("test1")
    lisichka_auth_page.press_button()
    assert lisichka_auth_page.find_error_message2() == "Неверный E-Mail или пароль"

def test_auth_id3(browser):
    lisichka_auth_page = Autorization(browser)
    lisichka_auth_page.go_to_site()
    lisichka_auth_page.enter_email("test@protei.ru")
    lisichka_auth_page.enter_password("")
    lisichka_auth_page.press_button()
    assert lisichka_auth_page.find_error_message2() == "Неверный E-Mail или пароль"

def test_auth_id4(browser):
    lisichka_auth_page = Autorization(browser)
    lisichka_auth_page.go_to_site()
    lisichka_auth_page.enter_email("test@protei.ru1")
    lisichka_auth_page.enter_password("test1")
    lisichka_auth_page.press_button()
    assert lisichka_auth_page.find_error_message2() == "Неверный E-Mail или пароль"

def test_auth_id5(browser):
    lisichka_auth_page = Autorization(browser)
    lisichka_auth_page.go_to_site()
    lisichka_auth_page.enter_email("test@protei.ru1")
    lisichka_auth_page.enter_password("")
    lisichka_auth_page.press_button()
    assert lisichka_auth_page.find_error_message2() == "Неверный E-Mail или пароль"

def test_auth_id6(browser):
    lisichka_auth_page = Autorization(browser)
    lisichka_auth_page.go_to_site()
    lisichka_auth_page.enter_email("test@protei.ru1")
    lisichka_auth_page.enter_password("")
    lisichka_auth_page.press_button()
    assert lisichka_auth_page.find_error_message2() == "Неверный E-Mail или пароль"

def test_auth_id7(browser):
    lisichka_auth_page = Autorization(browser)
    lisichka_auth_page.go_to_site()
    lisichka_auth_page.enter_email("")
    lisichka_auth_page.enter_password("")
    lisichka_auth_page.press_button()
    assert lisichka_auth_page.find_error_message() == "Неверный формат E-Mail"

def test_auth_id8(browser):
    lisichka_auth_page = Autorization(browser)
    lisichka_auth_page.go_to_site()
    lisichka_auth_page.enter_email("")
    lisichka_auth_page.enter_password("test")
    lisichka_auth_page.press_button()
    assert lisichka_auth_page.find_error_message() == "Неверный формат E-Mail"


