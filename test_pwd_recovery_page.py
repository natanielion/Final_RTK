import pytest
import time

from config.auth_data import valid_login


@pytest.mark.positive
@pytest.mark.structure
def test_pwd_recovery_page_has_correct_structure(browser, pwd_recovery_page):
    """Автоматизация по тест-кейсу: 10.
    Тест, который проверяет, что страница восстановления пароля открывается и содержит в себе все требуемые
    элементы: 4 таба выбора метода восстановления пароля (телефон, почта, логин, лицевой счет), форму ввода,
    картинку с капчей, форму для ввода капчи, кнопку "Продолжить" и кнопку "Вернуться"."""

    # Переходим на страницу восстановления пароля
    pwd_recovery_page.go_to_lk_auth_page()
    pwd_recovery_page.go_to_pwd_recovery_page()

    # Проверяем, что оказались на нужной странице и на ней присутствуют все необходимые элементы
    assert 'login-actions/reset-credentials' in browser.current_url, "Страница восстановления пароля не открылась"
    assert pwd_recovery_page.find_auto_selected_recovery_type() == "Телефон", \
        "По умолчанию выбрано не восстановление по Телефону"
    assert pwd_recovery_page.find_tab_recovery_by_phone(), "Не отображается таб восстановления пароля по телефону"
    assert pwd_recovery_page.find_tab_recovery_by_email(), "Не отображается таб восстановления пароля по почте"
    assert pwd_recovery_page.find_tab_recovery_by_login(), "Не отображается таб восстановления пароля по логину"
    assert pwd_recovery_page.find_tab_recovery_by_ls(), "Не отображается таб восстановления пароля по лицевому счету"
    assert pwd_recovery_page.find_input_field_username(), "Не отображается форма ввода телефона/почты/логина/ЛС"
    assert 'captcha' in pwd_recovery_page.find_captcha_image().get_attribute('src'), "Капча не отображается"
    assert pwd_recovery_page.find_captcha_input_field(), "Поле для вводы капчи не отображается"
    assert pwd_recovery_page.find_continue_recovery_btn().text == "Продолжить", \
        "Не отображается кнопка 'Продолжить' или она имеет другое название"
    assert pwd_recovery_page.find_go_back_to_recovery_page_btn().text == "Вернуться назад", \
        "Не отображается кнопка 'Вернуться назад' или она имеет другое название"


@pytest.mark.captcha
def test_recovery_method_choose_page_for_login_opens_with_correct_structure(browser, pwd_recovery_page):
    """Автоматизация по тест-кейсу: 11.
    Тест, который проверяет, что при вводе зарегистрированного в системе логина, к которому привязана и почта,
    и телефон, происходит переход на страницу с выбором метода восстановления пароля: по телефону или по почте.
    На странице присутствуют две радиокнопки с названиями методов восстановления, кнопка "Продолжить" и кнопка
    "Вернуться назад". В тесте требуется ручной ввод капчи, на который заложено 15 секунд."""

    # Переходим на страницу восстановления пароля
    pwd_recovery_page.go_to_lk_auth_page()
    pwd_recovery_page.go_to_pwd_recovery_page()

    # Кликаем по табу "Логин" для выбора соответствующего способа восстановления пароля,
    # вводим в него существующий логин с привязанными к нему почтой и телефоном, выставляем задержку для
    # ручного ввода капчи, после чего жмем на кнопку "Продолжить"
    pwd_recovery_page.click_on_tab_recovery_by_login()
    time.sleep(3)
    pwd_recovery_page.fill_input_field_username(valid_login)
    time.sleep(15)
    pwd_recovery_page.click_continue_recovery_btn()

    # Проверяем, что открылась форма выбора метода восстановления пароля и на ней есть все требуемые элементы
    assert len(pwd_recovery_page.find_radio_buttons_on_recovery_method_page()) == 2, \
        "На странице отсутствует одна из опций выбора или страница выбора метода восстановления пароля не открылась"
    assert pwd_recovery_page.find_radio_buttons_on_recovery_method_page()[0].text == "По номеру телефона", \
        "Отсутствует опция восстановления по телефону или она имеет другое название"
    assert pwd_recovery_page.find_radio_buttons_on_recovery_method_page()[1].text == "По e-mail", \
        "Отсутствует опция восстановления пароля по e-mail или она имеет другое название"
    assert pwd_recovery_page.find_continue_reset_pwd_btn().text == "Продолжить", \
        "Не отображается кнопка 'Продолжить' или она имеет другое название"
    assert pwd_recovery_page.find_cancel_pwd_reset_btn().text == "Вернуться назад", \
        "Не отображается кнопка 'Вернуться назад' или она имеет другое название"