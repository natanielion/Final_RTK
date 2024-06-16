import pytest
import time

from config.test_data_registration import incorrect_email_phone, incorrect_email_phone_ids, reg_email


@pytest.mark.positive
@pytest.mark.structure
def test_auth_with_code_page_has_correct_structure(browser, auth_with_code_page):
    """Автоматизация по тест-кейсу: 1.
    Тест, который проверяет, что на странице авторизации по коду присутствуют все требуемые элементы:
    подсказка по работе с формой (Укажите контактный номер телефона или почту, на которые необходимо
    отправить код подтверждения), поле ввода номера телефона или почты, а также кнопка "Получить код"."""

    # Открываем страницу ЛК, которая при неавторизованном режиме автоматически редиректит на форму
    # авторизации по коду
    auth_with_code_page.go_to_lk_auth_page()

    # Проверяем, что оказались на нужной странице и на ней есть все требуемые элементы
    assert 'protocol/openid-connect/auth' in browser.current_url, "Страница авторизации по коду не открылась"
    assert auth_with_code_page.find_card_description_text() == 'Укажите почту или номер телефона, на которые необходимо отправить код подтверждения', \
        "Отсутствует подсказка по работе с формой или она имеет другой текст"
    assert auth_with_code_page.find_input_field_for_code_auth(), "Не отображается поле для ввода номера телефона или почты"
    assert auth_with_code_page.find_send_code_button_auth().get_attribute('willValidate') == 'true', \
        "Кнопка 'Получить код' не активна"


@pytest.mark.captcha
def test_code_confirmation_page_has_correct_structure(browser, auth_with_code_page):
    """Автоматизация по тест-кейсу: 2.
    Тест, который проверяет, что на странице ввода кода подтверждения при авторизации по корректному формату
    почты присутствуют все требуемые элементы: почта, на которую был выслан код, ссылка "Изменить почту",
    шесть отдельных полей для ввода кода подтверждения, текст с обратным отсчетом времени до повторной попытки
    отправить код. Здесь возможно появление капчи, поэтому добавлена проверка на ее наличие и в случае, если капча есть,
    добавляется задержка 15 секунд после ввода e-mail для ее ручного ввода с клавиатуры."""

    # Открываем страницу ЛК, которая при неавторизованном режиме автоматически редиректит на форму
    # авторизации по коду
    auth_with_code_page.go_to_lk_auth_page()

    # Подставляем в поле "E-mail или мобильный телефон" корректный формат почты
    auth_with_code_page.fill_input_field_for_code_auth(reg_email)
    time.sleep(3)

    # Тут может появляться капча, поэтому добавляем ожидание для ввода текста с картинки
    try:
        auth_with_code_page.find_captcha_image_on_auth_with_code_page()
        time.sleep(15)
    except:
        pass

    auth_with_code_page.click_on_send_code_button_auth()

    # Проверяем, что попали на форму для ввода кода подтверждения и на ней есть все требуемые элементы
    assert auth_with_code_page.find_code_form_title_text() == "Код подтверждения отправлен", \
        "Переход на форму не был совершен или она имеет другой заголовок"
    assert reg_email in auth_with_code_page.find_email_in_code_form_description_text(), \
        "На странице не указан email, на который был выслан код"
    assert auth_with_code_page.count_code_input_fields() == 6, \
        "Недостаточно полей для ввода кода подтверждения (должно быть 6)"
    assert 'Изменить почту' in auth_with_code_page.find_change_email_link_in_code_form(), \
        "Отсутствует кнопка 'Изменить email'"
    assert 'numeric' in auth_with_code_page.check_code_input_fields_take_only_nums()


@pytest.mark.negative
@pytest.mark.parametrize('incorrect_email_phone', incorrect_email_phone, ids=incorrect_email_phone_ids)
def test_incorrect_password_alert_with_incorrect_data(browser, auth_with_code_page, incorrect_email_phone):
    """Автоматизация по тест-кейсу: 3.
    Тест, который проверяет поле формы "E-mail или мобильный телефон" на корректность обработки исключений,
    а также проверяет, что при некорректном заполнении поля выводится соответствующая подсказка."""

    # Открываем страницу ЛК, которая при неавторизованном режиме автоматически редиректит на форму
    # авторизации по коду
    auth_with_code_page.go_to_lk_auth_page()

    # Подставляем в поле "E-mail или мобильный телефон" параметры тестового сценария из фикстуры
    auth_with_code_page.fill_input_field_for_code_auth(incorrect_email_phone)
    time.sleep(2)
    auth_with_code_page.click_on_send_code_button_auth()

    # Ищем предупреждение под полем "E-mail или мобильный телефон"
    assert (auth_with_code_page.find_input_error_alert_text() ==
            'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'), \
        "Отсутствует предупреждение под полем 'E-mail или мобильный телефон'"


@pytest.mark.captcha
def test_change_email_on_code_confirmation_page(browser, auth_with_code_page):
    """Автоматизация по тест-кейсу: 4.
    Тест, который проверяет, что при вводе почты и запроса кода авторизации на нее и затем нажатия на
    кнопку "Изменить почту" происходит возврат к форме авторизации по коду и под полем для ввода почты или
    номера телефона появляется текст с отсчетом времени до возможности повторной отправки кода доступа. Здесь возможно
    появление капчи, поэтому добавлена проверка на ее наличие и в случае, если капча есть, добавляется задержка 15
    секунд после ввода e-mail для ее ручного ввода с клавиатуры."""

    # Открываем страницу ЛК, которая при неавторизованном режиме автоматически редиректит на форму
    # авторизации по коду
    auth_with_code_page.go_to_lk_auth_page()

    # Подставляем в поле "E-mail или мобильный телефон" корректный формат почты
    auth_with_code_page.fill_input_field_for_code_auth(reg_email)
    time.sleep(3)

    # Тут может появляться капча, поэтому добавляем ожидание для ввода текста с картинки
    try:
        auth_with_code_page.find_captcha_image_on_auth_with_code_page()
        time.sleep(15)
    except:
        pass

    auth_with_code_page.click_on_send_code_button_auth()

    # Проверяем, что попали на форму для ввода кода подтверждения, затем нажимаем на ссылку "Изменить почту"
    # и проверяем, что после этого оказываемся на форме авторизации по коду и под полем ввода почты есть текст
    # с отсчетом времени до возможности повторной отправки кода доступа
    assert auth_with_code_page.find_code_form_title_text() == "Код подтверждения отправлен", \
        "Переход на форму не был совершен или она имеет другой заголовок"

    time.sleep(3)
    auth_with_code_page.click_change_email_link_in_code_form()

    assert auth_with_code_page.find_input_field_for_code_auth(), \
        "Не был совершен переход на форму авторизации по коду или не отображается поле ввода почты"
    assert 'Отправка сообщения возможна через:' in auth_with_code_page.find_timeout_code_resend_alert_in_auth_form(), \
        "Текст с отсчетом времени до повторной отправки кода не отображается"