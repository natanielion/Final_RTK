from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RegistrationPage(BasePage):
    REG_LINK = (By.ID, 'kc-register')

    REG_NAME = (By.NAME, 'firstName')
    REG_SURNAME = (By.NAME, 'lastName')
    REG_EMAIL = (By.ID, 'address')
    REG_PASSWORD = (By.ID, 'password')
    REG_PASSW_CONFIRM = (By.ID, 'password-confirm')
    REG_BTN = (By.XPATH, '//section[@id="page-right"]//button[@name="register"]')

    REG_FIELDS = (By.XPATH, '//section[@id="page-right"]//input[contains(@class, "rt-input__input")]')
    LOGO_REG_PAGE = (By.XPATH, '//div[@class="what-is-container__logo-container"]')
    TITLE_REG_PAGE = (By.XPATH, '//section[@id="page-left"]//h2[@class="what-is__title"]')
    TAGLINE_REG_PAGE = (By.XPATH, '//section[@id="page-left"]//p[@class="what-is__desc"]')
    LEFT_SECTION_REG_PAGE = (By.ID, 'page-left')
    RIGHT_SECTION_REG_PAGE = (By.ID, 'page-right')
    USER_AGREEMENT_LINK = (By.ID, 'rt-auth-agreement-link')

    CONFIRMATION_TITLE = (By.XPATH, '//h1[@class="card-container__title"]')
    EMAIL_CONFIRM = (By.XPATH, '//p[@class="register-confirm-form-container__desc"]')
    CODE_CONFIRM = (By.CLASS_NAME, 'code-input__input')
    CHANGE_EMAIL = (By.XPATH, '//button[@name="otp_back_phone"]')
    CODE_TIMEOUT = (By.XPATH, '//span[@class="code-input-container__timeout"]')

    NAME_FIELD_ERROR = (By.XPATH, '//span[@class="rt-input-container__meta rt-input-container__meta--error"]')
    EMAIL_PHONE_ERROR = (By.XPATH, '//div[@class="register-form__address"]//span[@class="rt-input-container__meta rt-input-container__meta--error"]')
    PASSWORD_ERROR = (By.XPATH, '//div[@class="new-password-container"]/div[1]//span[@class="rt-input-container__meta rt-input-container__meta--error"]')
    PASSWORD_CONFIRM_ERROR = (By.XPATH, '//div[@class="new-password-container"]/div[2]//span[@class="rt-input-container__meta rt-input-container__meta--error"]')

    EMAIL_DUPLICATION_ERROR_TITLE = (By.XPATH, '//div[@class="card-modal__card"]/h2')
    EMAIL_DUPLICATION_ERROR_LOGIN_BTN = (By.NAME, 'gotoLogin')
    EMAIL_DUPLICATION_ERROR_RECOVER_LINK = (By.ID, 'reg-err-reset-pass')

    PHONE_DUPLICATION_ERROR_REG_NEW_ACC = (By.NAME, 'registration_confirm_btn')


    def go_to_registration_page(self):
        return self.find_element(self.REG_LINK).click()

    def find_name_field(self):
        return self.find_element(self.REG_NAME)

    def fill_name_field(self, value):
        return self.find_element(self.REG_NAME).send_keys(value)

    def find_surname_field(self):
        return self.find_element(self.REG_SURNAME)

    def fill_surname_field(self, value):
        return self.find_element(self.REG_SURNAME).send_keys(value)

    def find_email_field(self):
        return self.find_element(self.REG_EMAIL)

    def fill_email_field(self, value):
        return self.find_element(self.REG_EMAIL).send_keys(value)

    def find_password_field(self):
        return self.find_element(self.REG_PASSWORD)

    def fill_password_field(self, value):
        return self.find_element(self.REG_PASSWORD).send_keys(value)

    def find_password_confirmation_field(self):
        return self.find_element(self.REG_PASSW_CONFIRM)

    def fill_password_confirmation_field(self, value):
        return self.find_element(self.REG_PASSW_CONFIRM).send_keys(value)

    def find_registration_button(self):
        return self.find_element(self.REG_BTN)

    def click_registration_button(self):
        return self.find_element(self.REG_BTN).click()

    def count_registration_fields(self):
        fields = self.find_elements(self.REG_FIELDS)
        return len(fields)

    def find_logo_on_reg_page(self):
        return self.find_element(self.LOGO_REG_PAGE)

    def find_title_reg_page(self):
        return self.find_element(self.TITLE_REG_PAGE).text

    def find_tagline_reg_page(self):
        return self.find_element(self.TAGLINE_REG_PAGE).text

    def find_left_section_of_reg_page(self):
        return self.find_element(self.LEFT_SECTION_REG_PAGE)

    def find_right_section_of_reg_page(self):
        return self.find_element(self.RIGHT_SECTION_REG_PAGE)

    def find_user_agreement_link_on_reg_page(self):
        return self.find_element(self.USER_AGREEMENT_LINK).get_attribute('href')

    def find_confirmation_title(self):
        return self.find_element(self.CONFIRMATION_TITLE).text

    def find_email_on_confirmation_page(self):
        return self.find_element(self.EMAIL_CONFIRM).text

    def count_confirmation_code_fields(self):
        return len(self.find_elements(self.CODE_CONFIRM))

    def find_change_email_button(self):
        return self.find_element(self.CHANGE_EMAIL).text

    def find_code_timeout(self):
        return self.find_element(self.CODE_TIMEOUT).text

    def find_alert_under_name_field(self):
        return self.find_element(self.NAME_FIELD_ERROR).text

    def find_alert_under_email_phone_field(self):
        return self.find_element(self.EMAIL_PHONE_ERROR).text

    def find_alert_under_password_field(self):
        return self.find_element(self.PASSWORD_ERROR).text

    def find_alert_under_password_confirmation_field(self):
        return self.find_element(self.PASSWORD_CONFIRM_ERROR).text

    def find_email_duplication_alert_title(self):
        return self.find_element(self.EMAIL_DUPLICATION_ERROR_TITLE).text

    def find_email_duplication_alert_login_btn(self):
        return self.find_element(self.EMAIL_DUPLICATION_ERROR_LOGIN_BTN)

    def find_email_duplication_alert_recover_link(self):
        return self.find_element(self.EMAIL_DUPLICATION_ERROR_RECOVER_LINK).get_attribute('href')

    def find_phone_duplication_alert_register_new_acc(self):
        return self.find_element(self.PHONE_DUPLICATION_ERROR_REG_NEW_ACC)
