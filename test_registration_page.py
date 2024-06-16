import time
import pytest
from config.test_data_registration import *
from config.auth_data import *


@pytest.mark.positive
@pytest.mark.structure
def test_registration_page_has_correct_structure(browser, reg_page):
    """Частичная автоматизация по тест-кейсу: 12.
    Тест, который проверяет, что при нажатии на кнопку "Зарегистрироваться" открывается соответствующая
    страница, которая имеет требуемую структуру: она разделена на две части - в правой части есть форма регистрации
    с 6 полями (имя, фамилия, выбор региона, email/телефон, пароль, подтверждение пароля),
    в левой части есть логотип компании и продуктовый слоган."""

    # Открываем сначала страницу авторизации (т.к. у страницы регистрации нет прямой ссылки), затем переходим
    # на страницу авторизации
    reg_page.go_to_site()
    reg_page.go_to_registration_page()

    # Делаем проверки на то, что мы попали на страницу регистрации и она имеет структуру, соответствующую требованиям
    assert 'login-actions/registration' in browser.current_url, "Страница регистрации не открылась"
    assert reg_page.find_right_section_of_reg_page() and reg_page.find_left_section_of_reg_page(), \
        "Страница регистрации имеет некорректную структуру"
    assert reg_page.count_registration_fields() == 6, "Не отображается одно из полей формы регистрации"
    assert reg_page.find_logo_on_reg_page() != "", "Не отображается логотип компании"
    assert reg_page.find_title_reg_page() == "Личный кабинет", "Не отображается заголовок страницы (Личный кабинет)"
    assert reg_page.find_tagline_reg_page() == "Персональный помощник в цифровом мире Ростелекома", \
        "Не отображается продуктовый слоган"
    assert 'Зарегистрироваться' in reg_page.find_registration_button().text, \
        "Отсутствует кнопка 'Зарегистрироваться' или она имеет другой текст"
    assert reg_page.find_user_agreement_link_on_reg_page() == 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html', \
        "Отсутствует или некорректно указана ссылка на пользовательское соглашение"


@pytest.mark.positive
@pytest.mark.redirect
@pytest.mark.structure
def test_get_to_email_confirmation_page(browser, reg_page):
    """Автоматизация проверки промежуточной страницы по тест-кейсу: 13.
    Тест, который проверяет, что с корректно заполненными полями в форме регистрации
    происходит переход на страницу с ожиданием кода подтверждения, отправленного на почту,
    указанную при регистрации."""

    # Открываем сначала страницу авторизации (т.к. у страницы регистрации нет прямой ссылки), затем переходим
    # на страницу авторизации
    reg_page.go_to_site()
    reg_page.go_to_registration_page()

    # По очереди заполняем поля корректными данными
    # Между действиями добавляем задержки, чтобы система не заблокировала нас и не добавила капчу
    reg_page.fill_name_field(reg_name)
    time.sleep(1)
    reg_page.fill_surname_field(reg_surname)
    time.sleep(2)
    reg_page.fill_email_field(reg_email)
    time.sleep(1)
    reg_page.fill_password_field(reg_pass)
    time.sleep(1)
    reg_page.fill_password_confirmation_field(reg_pass)
    time.sleep(2)
    reg_page.click_registration_button()

    # Проверяем, что мы оказались на странице подтверждения email и на ней присутствуют все требуемые элементы
    assert 'login-actions/registration?execution' in browser.current_url, \
        "Не произошел переход на страницу подтверждения email"
    assert "Подтверждение email" in reg_page.find_confirmation_title(), \
        "На странице нет заголовка 'Подтверждение email'"
    assert reg_email in reg_page.find_email_on_confirmation_page(), \
        "На странице не указан email, по которому происходит регистрация"
    assert reg_page.count_confirmation_code_fields() == 6, \
        "Недостаточно полей для ввода кода подтверждения (должно быть 6)"
    assert 'Изменить email' in reg_page.find_change_email_button(), "Отсутствует кнопка 'Изменить email'"
    assert 'Получить код повторно' in reg_page.find_code_timeout(), "Отсутствует кнопка 'Получить код повторно'"


@pytest.mark.positive
@pytest.mark.redirect
@pytest.mark.structure
def test_get_to_phone_confirmation_page(browser, reg_page):
    """Автоматизация проверки промежуточной страницы по тест-кейсу: 14.
    Тест, который проверяет, что с корректно заполненными полями в форме регистрации
    происходит переход на страницу с ожиданием кода подтверждения, отправленного на номер телефона,
    указанный при регистрации."""

    # Открываем сначала страницу авторизации (т.к. у страницы регистрации нет прямой ссылки), затем переходим
    # на страницу авторизации
    reg_page.go_to_site()
    reg_page.go_to_registration_page()

    # По очереди заполняем поля корректными данными, в поле "E-mail или мобильный телефон" вводим телефон
    # Между действиями добавляем задержки, чтобы система не заблокировала нас и не добавила капчу
    reg_page.fill_name_field(reg_name)
    time.sleep(1)
    reg_page.fill_surname_field(reg_surname)
    time.sleep(2)
    reg_page.fill_email_field(reg_phone)
    time.sleep(1)
    reg_page.fill_password_field(reg_pass)
    time.sleep(1)
    reg_page.fill_password_confirmation_field(reg_pass)
    time.sleep(2)
    reg_page.click_registration_button()

    # Проверяем, что мы оказались на странице подтверждения телефона и на ней присутствуют все требуемые элементы
    assert 'login-actions/registration?execution' in browser.current_url, \
        "Не произошел переход на страницу подтверждения email"
    assert "Подтверждение телефона" in reg_page.find_confirmation_title(), \
        "На странице нет заголовка 'Подтверждение телефона'"
    assert reg_phone in reg_page.find_email_on_confirmation_page().replace(' ', '').replace('-', ''), \
        "На странице не указан номер телефона, по которому происходит регистрация"
    assert reg_page.count_confirmation_code_fields() == 6, \
        "Недостаточно полей для ввода кода подтверждения (должно быть 6)"
    assert 'Изменить номер' in reg_page.find_change_email_button(), "Отсутствует кнопка 'Изменить номер'"
    assert 'Получить код повторно' in reg_page.find_code_timeout(), "Отсутствует кнопка 'Получить код повторно'"


@pytest.mark.negative
@pytest.mark.parametrize('incorrect_name', incorrect_reg_names, ids=incorrect_reg_names_ids)
def test_not_redirect_to_email_confirmation_with_incorrect_name_field(browser, reg_page, incorrect_name):
    """Автоматизация по тест-кейсу: 15.
    Тест, который проверяет текстовые поля формы (на примере поля "Имя") на корректную обработку исключений,
    а также проверяет, что с некорректно заполненными полями в форме регистрации при нажатии на кнопку
    "Зарегистрироваться" не происходит переход на страницу подтверждения email и выводится соответствующее
    предупреждение под полем."""

    # Открываем сначала страницу авторизации (т.к. у страницы регистрации нет прямой ссылки), затем переходим
    # на страницу авторизации
    reg_page.go_to_site()
    reg_page.go_to_registration_page()

    # В поле "Имя" будут подставляться параметры тестового сценария из фикстуры
    # Остальные поля будут заполнены корректно
    reg_page.fill_name_field(incorrect_name)
    time.sleep(1)
    reg_page.fill_surname_field(reg_surname)
    time.sleep(2)
    reg_page.fill_email_field(reg_email)
    time.sleep(1)
    reg_page.fill_password_field(reg_pass)
    time.sleep(1)
    reg_page.fill_password_confirmation_field(reg_pass)
    time.sleep(2)
    reg_page.click_registration_button()

    # Проверяем, что остались на той же странице и ищем предупреждение под полем "Имя"
    assert 'login-actions/registration' in browser.current_url, "Текущая страница изменилась"
    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' in reg_page.find_alert_under_name_field(), \
        "Отсутствует предупреждение под полем 'Имя'"


@pytest.mark.negative
@pytest.mark.parametrize('incorrect_email_phone', incorrect_email_phone, ids=incorrect_email_phone_ids)
def test_not_redirect_to_email_confirmation_with_incorrect_email_and_phone_field(browser, reg_page, incorrect_email_phone):
    """Автоматизация по тест-кейсу: 16.
    Тест, который проверяет поле формы "E-mail или мобильный телефон" на корректность обработки исключений,
    а также проверяет, что с некорректно заполненными полями в форме регистрации при нажатии на кнопку
    "Зарегистрироваться" не происходит переход на страницу подтверждения email и выводится соответствующее
    предупреждение под полем."""

    # Открываем сначала страницу авторизации (т.к. у страницы регистрации нет прямой ссылки), затем переходим
    # на страницу авторизации
    reg_page.go_to_site()
    reg_page.go_to_registration_page()

    # В поле "E-mail или мобильный телефон" будут подставляться параметры тестового сценария из фикстуры
    # Остальные поля будут заполнены корректно
    reg_page.fill_name_field(reg_name)
    time.sleep(1)
    reg_page.fill_surname_field(reg_surname)
    time.sleep(2)
    reg_page.fill_email_field(incorrect_email_phone)
    time.sleep(1)
    reg_page.fill_password_field(reg_pass)
    time.sleep(1)
    reg_page.fill_password_confirmation_field(reg_pass)
    time.sleep(2)
    reg_page.click_registration_button()

    # Проверяем, что остались на той же странице и ищем предупреждение под полем "E-mail или мобильный телефон"
    assert 'login-actions/registration' in browser.current_url, "Текущая страница изменилась"
    assert ('Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru' in
            reg_page.find_alert_under_email_phone_field()), \
        "Отсутствует предупреждение под полем 'E-mail или мобильный телефон'"


@pytest.mark.negative
@pytest.mark.parametrize('incorrect_reg_pass, incorrect_reg_pass_expected_alert', incorrect_reg_pass_with_alerts, ids=incorrect_reg_pass_ids)
def test_not_redirect_to_email_confirmation_with_incorrect_password_field(browser, reg_page,
                                                                          incorrect_reg_pass,
                                                                          incorrect_reg_pass_expected_alert):
    """Автоматизация по тест-кейсу: 17.
    Тест, который проверяет поле "Пароль" на корректность обработки исключений, а также то, что при вводе пароля,
    не соответствующего требованиям, при нажатии на кнопку "Зарегистрироваться" не происходит переход на страницу
    подтверждения email и выводится соответствующее предупреждение под полем."""

    # Открываем сначала страницу авторизации (т.к. у страницы регистрации нет прямой ссылки), затем переходим
    # на страницу авторизации
    reg_page.go_to_site()
    reg_page.go_to_registration_page()

    # В поле "Пароль" будут подставляться параметры тестового сценария из фикстуры
    # Остальные поля будут заполнены корректно
    reg_page.fill_name_field(reg_name)
    time.sleep(1)
    reg_page.fill_surname_field(reg_surname)
    time.sleep(2)
    reg_page.fill_email_field(reg_email)
    time.sleep(1)
    reg_page.fill_password_field(incorrect_reg_pass)
    time.sleep(1)
    reg_page.fill_password_confirmation_field(incorrect_reg_pass)
    time.sleep(2)
    reg_page.click_registration_button()

    # Проверяем, что остались на той же странице и ищем предупреждение под полем "Пароль",
    # совпадающее с логикой требований к паролю
    assert 'login-actions/registration' in browser.current_url, "Текущая страница изменилась"
    assert incorrect_reg_pass_expected_alert in reg_page.find_alert_under_password_field(), \
        "Отсутствует предупреждение под полем 'Пароль' или оно не соответствует требуемому"


@pytest.mark.negative
def test_not_redirect_to_email_confirmation_with_mismatched_password_confirmation(browser, reg_page):
    """Автоматизация по тест-кейсу: 18.
    Тест, который проверяет, что при несовпадении пароля, введенного в поле "Подтверждение пароля",
    с паролем из поля "Пароль" при нажатии на кнопку "Зарегистрироваться" не происходит переход
    на страницу подтверждения email и выводится соответствующее предупреждение под полем."""

    # Открываем сначала страницу авторизации (т.к. у страницы регистрации нет прямой ссылки), затем переходим
    # на страницу авторизации
    reg_page.go_to_site()
    reg_page.go_to_registration_page()

    # По очереди заполняем поля корректными данными, кроме поля "Подтверждение пароля"
    reg_page.fill_name_field(reg_name)
    time.sleep(1)
    reg_page.fill_surname_field(reg_surname)
    time.sleep(2)
    reg_page.fill_email_field(reg_email)
    time.sleep(1)
    reg_page.fill_password_field(reg_pass)
    time.sleep(1)
    reg_page.fill_password_confirmation_field(reg_pass+'1')
    time.sleep(2)
    reg_page.click_registration_button()

    # Проверяем, что остались на той же странице и ищем предупреждение под полем "Подтверждение пароля"
    assert 'login-actions/registration' in browser.current_url, "Текущая страница изменилась"
    assert 'Пароли не совпадают' in reg_page.find_alert_under_password_confirmation_field(), \
        "Отсутствует предупреждение под полем 'Подтверждение пароля'"


@pytest.mark.negative
def test_not_redirect_to_email_confirmation_with_registered_email_reuse(browser, reg_page):
    """Автоматизация по тест-кейсу: 19.
    Тест, который проверяет, что при введении в форме регистрации email, который уже зарегистрирован
    в системе, форма выдаст соответствущее предупреждение и не произойдет переход на страницу подтверждения email."""

    # Открываем сначала страницу авторизации (т.к. у страницы регистрации нет прямой ссылки), затем переходим
    # на страницу авторизации
    reg_page.go_to_site()
    reg_page.go_to_registration_page()

    # По очереди заполняем поля корректными данными, в поле email вводим почту, уже зарегистрированную в системе
    reg_page.fill_name_field(reg_name)
    time.sleep(1)
    reg_page.fill_surname_field(reg_surname)
    time.sleep(2)
    reg_page.fill_email_field(valid_email)
    time.sleep(1)
    reg_page.fill_password_field(reg_pass)
    time.sleep(1)
    reg_page.fill_password_confirmation_field(reg_pass)
    time.sleep(2)
    reg_page.click_registration_button()

    # Проверяем, что остались на той же странице и поверх страницы появилась форма с предупреждением о
    # существовании аккаунта с таким email, на которой есть кнопка "Войти" и ссылка на восстановление пароля
    assert 'login-actions/registration' in browser.current_url, "Текущая страница изменилась"
    assert 'Учётная запись уже существует' in reg_page.find_email_duplication_alert_title(), \
        "Заголовок формы отсутствует или его текст не соответствует требуемому"
    assert 'Войти' in reg_page.find_email_duplication_alert_login_btn().text, \
        "Отсутствует кнопка 'Войти' или она имеет другой текст"
    assert 'login-actions/reset-credentials' in reg_page.find_email_duplication_alert_recover_link(), \
        "Отсутствует ссылка на восстановление пароля или она изменилась"


@pytest.mark.negative
def test_not_redirect_to_phone_confirmation_with_registered_phone_reuse(browser, reg_page):
    """Автоматизация по тест-кейсу: 20.
    Тест, который проверяет, что при введении в форме регистрации телефона, который уже зарегистрирован
    в системе, форма выдаст соответствущее предупреждение и не произойдет переход на страницу подтверждения телефона."""

    # Открываем сначала страницу авторизации (т.к. у страницы регистрации нет прямой ссылки), затем переходим
    # на страницу авторизации
    reg_page.go_to_site()
    reg_page.go_to_registration_page()

    # По очереди заполняем поля корректными данными, в поле email вводим телефон, уже зарегистрированный в системе
    reg_page.fill_name_field(reg_name)
    time.sleep(1)
    reg_page.fill_surname_field(reg_surname)
    time.sleep(2)
    reg_page.fill_email_field(valid_phone)
    time.sleep(1)
    reg_page.fill_password_field(reg_pass)
    time.sleep(1)
    reg_page.fill_password_confirmation_field(reg_pass)
    time.sleep(2)
    reg_page.click_registration_button()

    # Проверяем, что остались на той же странице и поверх страницы появилась форма с предупреждением о
    # существовании аккаунта с таким телефоном, на которой есть кнопка "Войти", ссылка на восстановление пароля
    # и кнопка "Зарегистрироваться"
    assert 'login-actions/registration' in browser.current_url, "Текущая страница изменилась"
    assert 'Учётная запись уже существует' in reg_page.find_email_duplication_alert_title(), \
        "Заголовок формы отсутствует или его текст не соответствует требуемому"
    assert 'Войти' in reg_page.find_email_duplication_alert_login_btn().text, \
        "Отсутствует кнопка 'Войти' или она имеет другой текст"
    assert 'login-actions/reset-credentials' in reg_page.find_email_duplication_alert_recover_link(), \
        "Отсутствует ссылка на восстановление пароля или она изменилась"
    assert 'Зарегистрироваться' in reg_page.find_phone_duplication_alert_register_new_acc().text, \
        "Отсутствует кнопка 'Зарегистрироваться' или она имеет другой текст"
