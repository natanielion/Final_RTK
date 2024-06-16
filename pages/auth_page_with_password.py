from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class FullAuthPage(BasePage):
    elk_page_url = 'https://start.rt.ru/?tab=main'
    FULL_AUTH_LINK = (By.ID, 'standard_auth_btn')

    AUTH_BY_PHONE = (By.ID, 't-btn-tab-phone')
    AUTH_BY_EMAIL = (By.ID, 't-btn-tab-mail')
    AUTH_BY_LOGIN = (By.ID, 't-btn-tab-login')
    AUTH_BY_PERSONAL_ACC = (By.ID, 't-btn-tab-ls')

    AUTO_SELECTED_AUTH_TYPE = (By.XPATH, '//div[@class="rt-tab rt-tab--small rt-tab--active"]')

    INPUT_USERNAME = (By.XPATH, '//input[@id="username"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@id="password"]')

    CHECKBOX_REMEMBER_ME = (By.XPATH, '//span[@class="rt-checkbox__shape rt-checkbox__shape--rounded rt-checkbox__shape--orange"]')
    CHECKBOX_REMEMBER_ME_TEXT = (By.XPATH, '//span[@class="rt-checkbox__label-desc"]')
    FORGOT_PWD_LINK = (By.ID, 'forgot_password')
    LOG_IN_BTN = (By.ID, 'kc-login')
    LOG_IN_BY_TEMP_CODE_BTN = (By.ID, 'back_to_otp_btn')

    LEFT_SECTION_AUTH_PAGE = (By.ID, 'page-left')
    RIGH_SECTION_AUTH_PAGE = (By.ID, 'page-right')
    TAGLINE_AUTH_PAGE = (By.XPATH, '//section[@id="page-left"]//p[@class="what-is__desc"]')

    USER_AGREEMENT_LINK = (By.ID, 'rt-auth-agreement-link')
    HELP_LINK = (By.XPATH, '//a[@class="rt-link rt-link--orange faq-modal-tip__btn"]')
    REGISTRATION_LINK = (By.ID, 'kc-register')

    ERROR_PWD_OR_ACC = (By.XPATH, '//div[@class="card-error login-form-container__error--bold"]')
    CAPTCHA_IMAGE = (By.XPATH, '//div[@class="rt-captcha__image-con"]')

    def go_to_full_auth_page(self):
        return self.find_element(self.FULL_AUTH_LINK).click()

    def find_auto_selected_auth_type(self):
        return self.find_element(self.AUTO_SELECTED_AUTH_TYPE).text

    def find_tagline_auth_page(self):
        return self.find_element(self.TAGLINE_AUTH_PAGE).text

    def find_left_section_of_auth_page(self):
        return self.find_element(self.LEFT_SECTION_AUTH_PAGE)

    def find_right_section_of_auth_page(self):
        return self.find_element(self.RIGH_SECTION_AUTH_PAGE)

    def find_user_agreement_link_on_auth_page(self):
        return self.find_element(self.USER_AGREEMENT_LINK).get_attribute('href')

    def find_questions_link_on_auth_page(self):
        return self.find_element(self.HELP_LINK)

    def find_tab_auth_by_phone(self):
        return self.find_element(self.AUTH_BY_PHONE)

    def find_tab_auth_by_email(self):
        return self.find_element(self.AUTH_BY_EMAIL)

    def find_tab_auth_by_login(self):
        return self.find_element(self.AUTH_BY_LOGIN)

    def find_tab_auth_by_personal_acc(self):
        return self.find_element(self.AUTH_BY_PERSONAL_ACC)

    def find_input_username_field(self):
        return self.find_element(self.INPUT_USERNAME)

    def fill_input_username_field(self, value):
        return self.find_element(self.INPUT_USERNAME).send_keys(value)

    def find_input_password_field(self):
        return self.find_element(self.INPUT_PASSWORD)

    def fill_input_password_field(self, value):
        return self.find_element(self.INPUT_PASSWORD).send_keys(value)

    def find_checkbox_remember_me(self):
        return self.find_element(self.CHECKBOX_REMEMBER_ME)

    def find_checkbox_remember_me_text(self):
        return self.find_element(self.CHECKBOX_REMEMBER_ME_TEXT).text

    def find_forgot_pwd_link_on_login_by_pwd_page(self):
        return self.find_element(self.FORGOT_PWD_LINK)

    def find_log_in_btn_on_login_by_pwd_page(self):
        return self.find_element(self.LOG_IN_BTN)

    def click_log_in_btn_on_login_by_pwd_page(self):
        return self.find_element(self.LOG_IN_BTN).click()

    def find_log_in_by_temp_code_btn(self):
        return self.find_element(self.LOG_IN_BY_TEMP_CODE_BTN)

    def find_registration_link_on_login_by_pwd_page(self):
        return self.find_element(self.REGISTRATION_LINK)

    def wait_elk_is_current_page(self):
        return WebDriverWait(self.driver, 10, 1).until(EC.url_to_be(self.elk_page_url))

    def get_class_name_of_forgot_pwd_link(self):
        return self.find_element(self.FORGOT_PWD_LINK).get_attribute('class')

    def find_error_pwd_or_account_message(self):
        return self.find_element(self.ERROR_PWD_OR_ACC).text

    def find_captcha_image_on_login_with_pwd_page(self):
        return self.find_element(self.CAPTCHA_IMAGE)