# Тестирование добавления пользователя
def test_auth_id1(GO_TO_ADD_USERS):
    lisichka_add_user = GO_TO_ADD_USERS
    lisichka_add_user.enter_email_in_add_user("test@protei.test")
    lisichka_add_user.enter_password_in_add_user("Protei123P")
    lisichka_add_user.enter_name_in_add_user("Gosha")
    lisichka_add_user.click_gender_in_add_user()
    lisichka_add_user.click_male_gender_in_add_user()
    lisichka_add_user.click_checkbox22_in_add_user()
    lisichka_add_user.click_checkbox23_in_add_user()
    lisichka_add_user.click_add_button_in_add_user()
    assert lisichka_add_user.search_user_added_in_add_user() == "Данные добавлены."
    lisichka_add_user.click_ok_in_dialog_message_in_add_user()


def test_auth_id2(GO_TO_ADD_USERS):
    lisichka_add_user = GO_TO_ADD_USERS
    lisichka_add_user.enter_email_in_add_user("test@protei.test")
    lisichka_add_user.enter_password_in_add_user("Protei123P")
    lisichka_add_user.enter_name_in_add_user("")
    lisichka_add_user.click_gender_in_add_user()
    lisichka_add_user.click_male_gender_in_add_user()
    lisichka_add_user.click_checkbox22_in_add_user()
    lisichka_add_user.click_checkbox23_in_add_user()
    lisichka_add_user.click_add_button_in_add_user()
    assert lisichka_add_user.search_null_name_error_in_add_user() == "Поле Имя не может быть пустым"

def test_auth_id3(GO_TO_ADD_USERS):
    lisichka_add_user = GO_TO_ADD_USERS
    lisichka_add_user.enter_email_in_add_user("test@protei.test")
    lisichka_add_user.enter_password_in_add_user("Protei123P")
    lisichka_add_user.enter_name_in_add_user("^8")
    lisichka_add_user.click_gender_in_add_user()
    lisichka_add_user.click_male_gender_in_add_user()
    lisichka_add_user.click_checkbox22_in_add_user()
    lisichka_add_user.click_checkbox23_in_add_user()
    lisichka_add_user.click_add_button_in_add_user()
    assert lisichka_add_user.search_null_name_error_in_add_user() == "Имя не может быть таким!"

def test_auth_id4(GO_TO_ADD_USERS):
    lisichka_add_user = GO_TO_ADD_USERS
    lisichka_add_user.enter_email_in_add_user("test@protei.test")
    lisichka_add_user.enter_password_in_add_user("")
    lisichka_add_user.enter_name_in_add_user("Gosha")
    lisichka_add_user.click_gender_in_add_user()
    lisichka_add_user.click_female_gender_in_add_user()
    lisichka_add_user.click_add_button_in_add_user()
    assert lisichka_add_user.search_null_password_error_in_add_user() == "Поле Пароль не может быть пустым"

def test_auth_id5(GO_TO_ADD_USERS):
    lisichka_add_user = GO_TO_ADD_USERS
    lisichka_add_user.enter_email_in_add_user("test@protei.test")
    lisichka_add_user.enter_password_in_add_user("")
    lisichka_add_user.enter_name_in_add_user("")
    lisichka_add_user.click_gender_in_add_user()
    lisichka_add_user.click_male_gender_in_add_user()
    lisichka_add_user.click_checkbox21_in_add_user()
    lisichka_add_user.click_checkbox22_in_add_user()
    lisichka_add_user.click_checkbox23_in_add_user()
    lisichka_add_user.click_add_button_in_add_user()
    assert lisichka_add_user.search_null_name_error_in_add_user() == "Поле Имя не может быть пустым"

def test_auth_id6(GO_TO_ADD_USERS):
    lisichka_add_user = GO_TO_ADD_USERS
    lisichka_add_user.enter_email_in_add_user("test@protei.test")
    lisichka_add_user.enter_password_in_add_user("")
    lisichka_add_user.enter_name_in_add_user("^@")
    lisichka_add_user.click_gender_in_add_user()
    lisichka_add_user.click_female_gender_in_add_user()
    lisichka_add_user.click_checkbox21_in_add_user()
    lisichka_add_user.click_checkbox22_in_add_user()
    lisichka_add_user.click_add_button_in_add_user()
    assert lisichka_add_user.search_null_password_error_in_add_user() == "Поле Пароль не может быть пустым"

def test_auth_id7(GO_TO_ADD_USERS):
    lisichka_add_user = GO_TO_ADD_USERS
    lisichka_add_user.enter_email_in_add_user("test@protei.test")
    lisichka_add_user.enter_password_in_add_user("1")
    lisichka_add_user.enter_name_in_add_user("Gosha")
    lisichka_add_user.click_gender_in_add_user()
    lisichka_add_user.click_male_gender_in_add_user()
    lisichka_add_user.click_checkbox21_in_add_user()
    lisichka_add_user.click_checkbox23_in_add_user()
    lisichka_add_user.click_add_button_in_add_user()
    assert lisichka_add_user.search_null_password_error_in_add_user() == "Пароль не может быть таким!"

def test_auth_id8(GO_TO_ADD_USERS):
    lisichka_add_user = GO_TO_ADD_USERS
    lisichka_add_user.enter_email_in_add_user("test@protei.test")
    lisichka_add_user.enter_password_in_add_user("1")
    lisichka_add_user.enter_name_in_add_user("")
    lisichka_add_user.click_gender_in_add_user()
    lisichka_add_user.click_female_gender_in_add_user()
    lisichka_add_user.click_checkbox21_in_add_user()
    lisichka_add_user.click_add_button_in_add_user()
    assert lisichka_add_user.search_null_name_error_in_add_user() == "Поле Имя не может быть пустым"

def test_auth_id9(GO_TO_ADD_USERS):
    lisichka_add_user = GO_TO_ADD_USERS
    lisichka_add_user.enter_email_in_add_user("test@protei.test")
    lisichka_add_user.enter_password_in_add_user("1")
    lisichka_add_user.enter_name_in_add_user("1")
    lisichka_add_user.click_gender_in_add_user()
    lisichka_add_user.click_male_gender_in_add_user()
    lisichka_add_user.click_radiobutton12_in_add_user()
    lisichka_add_user.click_checkbox22_in_add_user()
    lisichka_add_user.click_checkbox23_in_add_user()
    lisichka_add_user.click_add_button_in_add_user()
    assert lisichka_add_user.search_null_name_error_in_add_user() == "Имя не может быть таким!"

def test_auth_id10(GO_TO_ADD_USERS):
    lisichka_add_user = GO_TO_ADD_USERS
    lisichka_add_user.enter_email_in_add_user("")
    lisichka_add_user.enter_password_in_add_user("123456")
    lisichka_add_user.enter_name_in_add_user("Gosha")
    lisichka_add_user.click_gender_in_add_user()
    lisichka_add_user.click_female_gender_in_add_user()
    lisichka_add_user.click_radiobutton12_in_add_user()
    lisichka_add_user.click_checkbox22_in_add_user()
    lisichka_add_user.click_add_button_in_add_user()
    assert lisichka_add_user.search_email_format_error_in_add_user() == "Неверный формат E-Mail"

def test_auth_id11(GO_TO_ADD_USERS):
    lisichka_add_user = GO_TO_ADD_USERS
    lisichka_add_user.enter_email_in_add_user("")
    lisichka_add_user.enter_password_in_add_user("123456")
    lisichka_add_user.enter_name_in_add_user("")
    lisichka_add_user.click_gender_in_add_user()
    lisichka_add_user.click_male_gender_in_add_user()
    lisichka_add_user.click_radiobutton12_in_add_user()
    lisichka_add_user.click_checkbox23_in_add_user()
    lisichka_add_user.click_add_button_in_add_user()
    assert lisichka_add_user.search_email_format_error_in_add_user() == "Неверный формат E-Mail"

def test_auth_id12(GO_TO_ADD_USERS):
    lisichka_add_user = GO_TO_ADD_USERS
    lisichka_add_user.enter_email_in_add_user("")
    lisichka_add_user.enter_password_in_add_user("123456")
    lisichka_add_user.enter_name_in_add_user("^@2")
    lisichka_add_user.click_gender_in_add_user()
    lisichka_add_user.click_female_gender_in_add_user()
    lisichka_add_user.click_radiobutton12_in_add_user()
    lisichka_add_user.click_add_button_in_add_user()
    assert lisichka_add_user.search_email_format_error_in_add_user() == "Неверный формат E-Mail"

def test_auth_id13(GO_TO_ADD_USERS):
    lisichka_add_user = GO_TO_ADD_USERS
    lisichka_add_user.enter_email_in_add_user("^@^")
    lisichka_add_user.enter_password_in_add_user("")
    lisichka_add_user.enter_name_in_add_user("Gosha")
    lisichka_add_user.click_gender_in_add_user()
    lisichka_add_user.click_male_gender_in_add_user()
    lisichka_add_user.click_radiobutton12_in_add_user()
    lisichka_add_user.click_checkbox22_in_add_user()
    lisichka_add_user.click_checkbox23_in_add_user()
    lisichka_add_user.click_add_button_in_add_user()
    assert lisichka_add_user.search_email_format_error_in_add_user() == "Неверный формат E-Mail"

def test_auth_id14(GO_TO_ADD_USERS):
    lisichka_add_user = GO_TO_ADD_USERS
    lisichka_add_user.enter_email_in_add_user("")
    lisichka_add_user.enter_password_in_add_user("")
    lisichka_add_user.enter_name_in_add_user("")
    lisichka_add_user.click_gender_in_add_user()
    lisichka_add_user.click_female_gender_in_add_user()
    lisichka_add_user.click_radiobutton12_in_add_user()
    lisichka_add_user.click_checkbox21_in_add_user()
    lisichka_add_user.click_checkbox22_in_add_user()
    lisichka_add_user.click_add_button_in_add_user()
    assert lisichka_add_user.search_email_format_error_in_add_user() == "Неверный формат E-Mail"

def test_auth_id15(GO_TO_ADD_USERS):
    lisichka_add_user = GO_TO_ADD_USERS
    lisichka_add_user.enter_email_in_add_user("")
    lisichka_add_user.enter_password_in_add_user("")
    lisichka_add_user.enter_name_in_add_user("^@")
    lisichka_add_user.click_gender_in_add_user()
    lisichka_add_user.click_male_gender_in_add_user()
    lisichka_add_user.click_radiobutton12_in_add_user()
    lisichka_add_user.click_checkbox21_in_add_user()
    lisichka_add_user.click_checkbox22_in_add_user()
    lisichka_add_user.click_add_button_in_add_user()
    assert lisichka_add_user.search_email_format_error_in_add_user() == "Неверный формат E-Mail"

def test_auth_id16(GO_TO_ADD_USERS):
    lisichka_add_user = GO_TO_ADD_USERS
    lisichka_add_user.enter_email_in_add_user("")
    lisichka_add_user.enter_password_in_add_user("1")
    lisichka_add_user.enter_name_in_add_user("Gosha")
    lisichka_add_user.click_gender_in_add_user()
    lisichka_add_user.click_female_gender_in_add_user()
    lisichka_add_user.click_radiobutton12_in_add_user()
    lisichka_add_user.click_checkbox21_in_add_user()
    lisichka_add_user.click_checkbox23_in_add_user()
    lisichka_add_user.click_add_button_in_add_user()
    assert lisichka_add_user.search_email_format_error_in_add_user() == "Неверный формат E-Mail"

def test_auth_id17(GO_TO_ADD_USERS):
    lisichka_add_user = GO_TO_ADD_USERS
    lisichka_add_user.enter_email_in_add_user("")
    lisichka_add_user.enter_password_in_add_user("1")
    lisichka_add_user.enter_name_in_add_user("")
    lisichka_add_user.click_gender_in_add_user()
    lisichka_add_user.click_male_gender_in_add_user()
    lisichka_add_user.click_radiobutton12_in_add_user()
    lisichka_add_user.click_checkbox22_in_add_user()
    lisichka_add_user.click_checkbox23_in_add_user()
    lisichka_add_user.click_add_button_in_add_user()
    assert lisichka_add_user.search_email_format_error_in_add_user() == "Неверный формат E-Mail"

def test_auth_id18(GO_TO_ADD_USERS):
    lisichka_add_user = GO_TO_ADD_USERS
    lisichka_add_user.enter_email_in_add_user("")
    lisichka_add_user.enter_password_in_add_user("1")
    lisichka_add_user.enter_name_in_add_user("^@")
    lisichka_add_user.click_gender_in_add_user()
    lisichka_add_user.click_female_gender_in_add_user()
    lisichka_add_user.click_checkbox22_in_add_user()
    lisichka_add_user.click_add_button_in_add_user()
    assert lisichka_add_user.search_email_format_error_in_add_user() == "Неверный формат E-Mail"

def test_auth_id19(GO_TO_ADD_USERS):
    lisichka_add_user = GO_TO_ADD_USERS
    lisichka_add_user.enter_email_in_add_user("^@")
    lisichka_add_user.enter_password_in_add_user("123456")
    lisichka_add_user.enter_name_in_add_user("Gosha")
    lisichka_add_user.click_gender_in_add_user()
    lisichka_add_user.click_male_gender_in_add_user()
    lisichka_add_user.click_radiobutton12_in_add_user()
    lisichka_add_user.click_checkbox23_in_add_user()
    lisichka_add_user.click_add_button_in_add_user()
    assert lisichka_add_user.search_email_format_error_in_add_user() == "Неверный формат E-Mail"

def test_auth_id20(GO_TO_ADD_USERS):
    lisichka_add_user = GO_TO_ADD_USERS
    lisichka_add_user.enter_email_in_add_user("^@")
    lisichka_add_user.enter_password_in_add_user("123456")
    lisichka_add_user.enter_name_in_add_user("")
    lisichka_add_user.click_gender_in_add_user()
    lisichka_add_user.click_female_gender_in_add_user()
    lisichka_add_user.click_add_button_in_add_user()
    assert lisichka_add_user.search_email_format_error_in_add_user() == "Неверный формат E-Mail"

def test_auth_id21(GO_TO_ADD_USERS):
    lisichka_add_user = GO_TO_ADD_USERS
    lisichka_add_user.enter_email_in_add_user("^@")
    lisichka_add_user.enter_password_in_add_user("123456")
    lisichka_add_user.enter_name_in_add_user("^@")
    lisichka_add_user.click_gender_in_add_user()
    lisichka_add_user.click_male_gender_in_add_user()
    lisichka_add_user.click_radiobutton12_in_add_user()
    lisichka_add_user.click_checkbox21_in_add_user()
    lisichka_add_user.click_checkbox22_in_add_user()
    lisichka_add_user.click_checkbox23_in_add_user()
    lisichka_add_user.click_add_button_in_add_user()
    assert lisichka_add_user.search_email_format_error_in_add_user() == "Неверный формат E-Mail"

def test_auth_id22(GO_TO_ADD_USERS):
    lisichka_add_user = GO_TO_ADD_USERS
    lisichka_add_user.enter_email_in_add_user("^@")
    lisichka_add_user.enter_password_in_add_user("")
    lisichka_add_user.enter_name_in_add_user("Gosha")
    lisichka_add_user.click_gender_in_add_user()
    lisichka_add_user.click_female_gender_in_add_user()
    lisichka_add_user.click_checkbox21_in_add_user()
    lisichka_add_user.click_checkbox22_in_add_user()
    lisichka_add_user.click_add_button_in_add_user()
    assert lisichka_add_user.search_email_format_error_in_add_user() == "Неверный формат E-Mail"

def test_auth_id23(GO_TO_ADD_USERS):
    lisichka_add_user = GO_TO_ADD_USERS
    lisichka_add_user.enter_email_in_add_user("^@")
    lisichka_add_user.enter_password_in_add_user("")
    lisichka_add_user.enter_name_in_add_user("")
    lisichka_add_user.click_gender_in_add_user()
    lisichka_add_user.click_male_gender_in_add_user()
    lisichka_add_user.click_radiobutton12_in_add_user()
    lisichka_add_user.click_checkbox21_in_add_user()
    lisichka_add_user.click_checkbox23_in_add_user()
    lisichka_add_user.click_add_button_in_add_user()
    assert lisichka_add_user.search_email_format_error_in_add_user() == "Неверный формат E-Mail"

def test_auth_id24(GO_TO_ADD_USERS):
    lisichka_add_user = GO_TO_ADD_USERS
    lisichka_add_user.enter_email_in_add_user("^@")
    lisichka_add_user.enter_password_in_add_user("")
    lisichka_add_user.enter_name_in_add_user("^@")
    lisichka_add_user.click_gender_in_add_user()
    lisichka_add_user.click_female_gender_in_add_user()
    lisichka_add_user.click_checkbox21_in_add_user()
    lisichka_add_user.click_add_button_in_add_user()
    assert lisichka_add_user.search_email_format_error_in_add_user() == "Неверный формат E-Mail"

def test_auth_id25(GO_TO_ADD_USERS):
    lisichka_add_user = GO_TO_ADD_USERS
    lisichka_add_user.enter_email_in_add_user("^@")
    lisichka_add_user.enter_password_in_add_user("")
    lisichka_add_user.enter_name_in_add_user("Gosha")
    lisichka_add_user.click_gender_in_add_user()
    lisichka_add_user.click_male_gender_in_add_user()
    lisichka_add_user.click_radiobutton12_in_add_user()
    lisichka_add_user.click_radiobutton11_in_add_user()
    lisichka_add_user.click_checkbox22_in_add_user()
    lisichka_add_user.click_checkbox23_in_add_user()
    lisichka_add_user.click_add_button_in_add_user()
    assert lisichka_add_user.search_email_format_error_in_add_user() == "Неверный формат E-Mail"

def test_auth_id26(GO_TO_ADD_USERS):
    lisichka_add_user = GO_TO_ADD_USERS
    lisichka_add_user.enter_email_in_add_user("^@")
    lisichka_add_user.enter_password_in_add_user("^@")
    lisichka_add_user.enter_name_in_add_user("")
    lisichka_add_user.click_gender_in_add_user()
    lisichka_add_user.click_female_gender_in_add_user()
    lisichka_add_user.click_checkbox22_in_add_user()
    lisichka_add_user.click_add_button_in_add_user()
    assert lisichka_add_user.search_email_format_error_in_add_user() == "Неверный формат E-Mail"

def test_auth_id27(GO_TO_ADD_USERS):
    lisichka_add_user = GO_TO_ADD_USERS
    lisichka_add_user.enter_email_in_add_user("^@")
    lisichka_add_user.enter_password_in_add_user("^@")
    lisichka_add_user.enter_name_in_add_user("^@")
    lisichka_add_user.click_gender_in_add_user()
    lisichka_add_user.click_male_gender_in_add_user()
    lisichka_add_user.click_radiobutton12_in_add_user()
    lisichka_add_user.click_checkbox23_in_add_user()
    lisichka_add_user.click_add_button_in_add_user()
    assert lisichka_add_user.search_email_format_error_in_add_user() == "Неверный формат E-Mail"

def test_auth_id28(GO_TO_ADD_USERS):
    lisichka_add_user = GO_TO_ADD_USERS
    lisichka_add_user.enter_email_in_add_user("test@protei.ru")
    lisichka_add_user.enter_password_in_add_user("Protei123P")
    lisichka_add_user.enter_name_in_add_user("Gosha")
    lisichka_add_user.click_gender_in_add_user()
    lisichka_add_user.click_female_gender_in_add_user()
    lisichka_add_user.click_radiobutton12_in_add_user()
    lisichka_add_user.click_checkbox21_in_add_user()
    lisichka_add_user.click_add_button_in_add_user()
    assert lisichka_add_user.search_user_added_in_add_user() == "Данные добавлены."
    lisichka_add_user.click_ok_in_dialog_message_in_add_user()
