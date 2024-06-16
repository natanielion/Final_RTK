import pytest
import time
from config.auth_data import valid_login, valid_phone, valid_password_for_phone, new_valid_password
from config.test_data_registration import reg_pass, reg_email


@pytest.mark.positive
@pytest.mark.structure
def test_full_auth_page_has_correct_structure(browser, auth_with_password_page):
    """Автоматизация по тест-кейсу: 5.
    Тест, который проверяет, что страница регистрации по номеру телефона/почте/логину или ЛС имеет
    структуру, соответствующую требованиям, и на ней присутствуют все необходимые поля, ссылки и элементы:
    страница поделена на две части, в правой части есть меню выбора типа аутентификации (автоматически выбран
    тип "Телефон"), есть форма ввода логина/телефона/почты/лицевого счета, есть форма ввода пароля, чекбокс "Запомнить
    меня", ссылка "Забыл пароль", кнопка "Войти", кнопка "Войти по временному коду" и есть вспомогательная информация.
    В левой части есть продуктовый слоган ЛК Ростелеком."""

    # Открываем сначала страницу тестируемого продукта - ЕЛК Web, после чего переходим
    # на страницу "Войти с паролем"
    auth_with_password_page.go_to_lk_auth_page()
    auth_with_password_page.go_to_full_auth_page()

    # Делаем проверки на то, что мы попали на страницу авторизации с паролем
    # и она имеет структуру, соответствующую требованиям
    assert 'login-actions/authenticate' in browser.current_url, "Страница авторизации по паролю не открылась"
    assert auth_with_password_page.find_right_section_of_auth_page() and auth_with_password_page.find_left_section_of_auth_page(), \
        "Страница авторизации с паролем имеет некорректную структуру"
    assert auth_with_password_page.find_tagline_auth_page() == "Персональный помощник в цифровом мире Ростелекома", \
        "Не отображается продуктовый слоган"
    assert (auth_with_password_page.find_tab_auth_by_phone() and auth_with_password_page.find_tab_auth_by_email() and
            auth_with_password_page.find_tab_auth_by_login() and auth_with_password_page.find_tab_auth_by_personal_acc()), \
        "Не хватает одной из вкладок с выбором типа авторизации"
    assert auth_with_password_page.find_auto_selected_auth_type() == 'Телефон', \
        "Автоматически выбран не тип авторизации 'по Телефону'"
    assert auth_with_password_page.find_input_username_field() and auth_with_password_page.find_input_password_field(), \
        "Не отображается одно из полей для ввода данных авторизации"
    assert auth_with_password_page.find_checkbox_remember_me(), "Не отображается чекбокс 'Запомнить меня'"
    assert auth_with_password_page.find_checkbox_remember_me_text() == 'Запомнить меня', \
        "Не отображается текст чекбокса 'Запомнить меня'"
    assert auth_with_password_page.find_forgot_pwd_link_on_login_by_pwd_page().text == "Забыл пароль", \
        "Не отображается кнопка 'Забыл пароль' или она имеет другое название"
    assert auth_with_password_page.find_log_in_btn_on_login_by_pwd_page().text == "Войти", \
        "Не отображается кнопка 'Войти' или она имеет другое название"
    assert auth_with_password_page.find_log_in_by_temp_code_btn().text == "Войти по временному коду", \
        "Не отображается кнопка 'Войти по временному коду' или она имеет другое название"
    assert (auth_with_password_page.find_user_agreement_link_on_auth_page() ==
            'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'), \
        "Отсутствует или некорректно указана ссылка на пользовательское соглашение"
    assert auth_with_password_page.find_registration_link_on_login_by_pwd_page().text == "Зарегистрироваться", \
        "Не отображается ссылка на регистрацию или она имеет другое название"
    assert auth_with_password_page.find_questions_link_on_auth_page().text == 'Помощь', \
        "Отсутствует или переименована кнопка 'Помощь' на странице авторизации"


@pytest.mark.positive
def test_auth_tab_switched_to_relevant_for_input(browser, auth_with_password_page):
    """Автоматизация по тест-кейсу: 6.
    Тест, который проверяет, что при выбранном по умолчанию табе типа аутентификации "Телефон" и вводе в поле
    "Мобильный телефон" логина, таб аутентификации автоматически переключается на "Логин"."""

    # Открываем сначала страницу тестируемого продукта - ЕЛК Web, после чего переходим
    # на страницу "Войти с паролем"
    auth_with_password_page.go_to_lk_auth_page()
    auth_with_password_page.go_to_full_auth_page()

    # Проверяем, что сейчас выбран таб "Телефон"
    assert auth_with_password_page.find_auto_selected_auth_type() == 'Телефон', \
        "Автоматически выбран не тип авторизации 'по Телефону'"

    time.sleep(2)
    auth_with_password_page.fill_input_username_field(valid_login)
    time.sleep(1)
    auth_with_password_page.find_input_password_field().click()
    time.sleep(2)

    # Проверяем, что теперь автоматически выбран там "Логин"
    assert auth_with_password_page.find_auto_selected_auth_type() == 'Логин', \
        "Таб аутентификации не переключился на 'Логин'"


@pytest.mark.captcha
def test_elk_page_opens_with_correct_phone_and_password(browser, auth_with_password_page):
    """Автоматизация по тест-кейсу: 7.
    Тест, который проверяет, что при вводе корректного зарегистрированного в системе телефона и соответствующего
    ему пароля, после нажатия на кнопку "Войти" происходит переход на страницу ЕЛК Web. Здесь возможно появление капчи,
    поэтому добавлена проверка на ее наличие и в случае, если капча есть, добавляется задержка 15 секунд после ввода
    пароля для ее ручного ввода с клавиатуры."""

    # Открываем сначала страницу тестируемого продукта - ЕЛК Web, после чего переходим
    # на страницу "Войти с паролем"
    auth_with_password_page.go_to_lk_auth_page()
    auth_with_password_page.go_to_full_auth_page()

    # Вводим данные для аутентификации и жмем кнопку "Войти"
    time.sleep(1)
    auth_with_password_page.fill_input_username_field(valid_phone)
    time.sleep(2)
    auth_with_password_page.fill_input_password_field(valid_password_for_phone)
    time.sleep(2)

    # Тут может появляться капча, поэтому добавляем ожидание для ввода текста с картинки
    try:
        auth_with_password_page.find_captcha_image_on_login_with_pwd_page()
        time.sleep(15)
    except:
        pass

    auth_with_password_page.click_log_in_btn_on_login_by_pwd_page()

    # Проверяем, что открылась страница ЕЛК Web
    assert auth_with_password_page.wait_elk_is_current_page(), "Страница ЕЛК Web не открылась или имеет другой url"


@pytest.mark.captcha
def test_not_redirect_to_elk_page_with_incorrect_pwd_shows_message(browser, auth_with_password_page):
    """Автоматизация по тест-кейсу: 8.
    Тест, который проверяет, что при вводе корректного зарегистрированного в системе логина, к которому привязана
    только почта, и некорректного пароля не происходит переход переход на страницу ЕЛК Web, над формой аутентификации
    появляется соответствующее сообщение и кнопка "Забыл пароль" меняет цвет на оранжевый. Здесь возможно появление
    капчи, поэтому добавлена проверка на ее наличие и в случае, если капча есть, добавляется задержка 15 секунд после
    ввода пароля для ее ручного ввода с клавиатуры."""

    # Открываем сначала страницу тестируемого продукта - ЕЛК Web, после чего переходим
    # на страницу "Войти с паролем"
    auth_with_password_page.go_to_lk_auth_page()
    auth_with_password_page.go_to_full_auth_page()

    # Переходим в тип аутентификации "Логин", вводим данные для аутентификации
    # (корректный логин и некорректный пароль) и жмем кнопку "Войти"
    auth_with_password_page.find_tab_auth_by_login().click()
    time.sleep(1)
    auth_with_password_page.fill_input_username_field(valid_login)
    time.sleep(2)
    auth_with_password_page.fill_input_password_field(reg_pass)
    time.sleep(2)

    # Тут может появляться капча, поэтому добавляем ожидание для ввода текста с картинки
    try:
        auth_with_password_page.find_captcha_image_on_login_with_pwd_page()
        time.sleep(15)
    except:
        pass

    auth_with_password_page.click_log_in_btn_on_login_by_pwd_page()

    # Проверяем, что остались на той же странице, появилось предупреждение над формой и кнопка "Забыл пароль" стала
    # оранжевой
    assert 'login-actions/authenticate' in browser.current_url, "URL страницы изменился"
    assert auth_with_password_page.find_error_pwd_or_account_message() == "Неверный логин или пароль", \
        "Сообщение об ошибке не отображается или имеет другой текст"
    assert (auth_with_password_page.get_class_name_of_forgot_pwd_link() ==
            "rt-link rt-link--orange login-form__forgot-pwd login-form__forgot-pwd--animated"), \
        "Кнопка 'Забыл пароль' не изменилась или изменения отличаются от требуемых"


@pytest.mark.captcha
def test_not_redirect_to_elk_page_with_unregistered_email_shows_message(browser, auth_with_password_page):
    """Автоматизация по тест-кейсу: 9.
    Тест, который проверяет, что при попытке входа по незарегистрированному в системе email и реальному паролю от
    действующей учетной записи не происходит переход переход на страницу ЕЛК Web, над формой аутентификации
    появляется соответствующее сообщение и кнопка "Забыл пароль" меняет цвет на оранжевый. Здесь возможно появление
    капчи, поэтому добавлена проверка на ее наличие и в случае, если капча есть, добавляется задержка 15 секунд после
    ввода пароля для ее ручного ввода с клавиатуры."""

    # Открываем сначала страницу тестируемого продукта - ЕЛК Web, после чего переходим
    # на страницу "Войти с паролем"
    auth_with_password_page.go_to_lk_auth_page()
    auth_with_password_page.go_to_full_auth_page()

    # Переходим в тип аутентификации "Почта", вводим данные для аутентификации
    # (незарегистрированная в системе почта и пароль от действующей учетной записи) и жмем кнопку "Войти"
    auth_with_password_page.find_tab_auth_by_email().click()
    time.sleep(1)
    auth_with_password_page.fill_input_username_field(reg_email)
    time.sleep(2)
    auth_with_password_page.fill_input_password_field(new_valid_password)
    time.sleep(2)

    # Тут может появляться капча, поэтому добавляем ожидание для ввода текста с картинки
    try:
        auth_with_password_page.find_captcha_image_on_login_with_pwd_page()
        time.sleep(15)
    except:
        pass

    auth_with_password_page.click_log_in_btn_on_login_by_pwd_page()

    # Проверяем, что остались на той же странице, появилось предупреждение над формой и кнопка "Забыл пароль" стала
    # оранжевой
    assert 'login-actions/authenticate' in browser.current_url, "URL страницы изменился"
    assert auth_with_password_page.find_error_pwd_or_account_message() == "Неверный логин или пароль", \
        "Сообщение об ошибке не отображается или имеет другой текст"
    assert (auth_with_password_page.get_class_name_of_forgot_pwd_link() ==
            "rt-link rt-link--orange login-form__forgot-pwd login-form__forgot-pwd--animated"), \
        "Кнопка 'Забыл пароль' не изменилась или изменения отличаются от требуемых"