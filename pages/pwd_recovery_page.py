from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class PasswordRecoveryPage(BasePage):
    FULL_AUTH_LINK = (By.ID, 'standard_auth_btn')
    PWD_RECOVERY_LINK = (By.ID, 'forgot_password')

    TAB_RECOVERY_BY_PHONE = (By.ID, 't-btn-tab-phone')
    TAB_RECOVERY_BY_EMAIL = (By.ID, 't-btn-tab-mail')
    TAB_RECOVERY_BY_LOGIN = (By.ID, 't-btn-tab-login')
    TAB_RECOVERY_BY_LS = (By.ID, 't-btn-tab-ls')
    AUTO_SELECTED_RECOVERY_TYPE = (By.XPATH, '//div[@class="rt-tab rt-tab--small rt-tab--active"]')

    INPUT_FIELD_USERNAME = (By.ID, 'username')
    CAPTCHA_IMAGE = (By.CLASS_NAME, 'rt-captcha__image')
    CAPTCHA_INPUT_FIELD = (By.ID, 'captcha')
    CONTINUE_BTN = (By.ID, 'reset')
    GO_BACK_BTN = (By.ID, 'reset-back')

    RADIO_BUTTONS = (By.XPATH, '//span[@class="rt-radio__label"]')
    CONTINUE_BTN_2_STAGE = (By.ID, 'reset-form-submit')
    CANCEL_RESET_BTN = (By.ID, 'reset-form-cancel')

    def go_to_pwd_recovery_page(self):
        self.find_element(self.FULL_AUTH_LINK).click()
        return self.find_element(self.PWD_RECOVERY_LINK).click()

    def find_tab_recovery_by_phone(self):
        return self.find_element(self.TAB_RECOVERY_BY_PHONE)

    def find_tab_recovery_by_email(self):
        return self.find_element(self.TAB_RECOVERY_BY_EMAIL)

    def find_tab_recovery_by_login(self):
        return self.find_element(self.TAB_RECOVERY_BY_LOGIN)

    def click_on_tab_recovery_by_login(self):
        return self.find_element(self.TAB_RECOVERY_BY_LOGIN)

    def find_tab_recovery_by_ls(self):
        return self.find_element(self.TAB_RECOVERY_BY_LS)

    def find_auto_selected_recovery_type(self):
        return self.find_element(self.AUTO_SELECTED_RECOVERY_TYPE).text

    def find_input_field_username(self):
        return self.find_element(self.INPUT_FIELD_USERNAME)

    def fill_input_field_username(self, value):
        return self.find_element(self.INPUT_FIELD_USERNAME).send_keys(value)

    def find_captcha_image(self):
        return self.find_element(self.CAPTCHA_IMAGE)

    def find_captcha_input_field(self):
        return self.find_element(self.CAPTCHA_INPUT_FIELD)

    def find_continue_recovery_btn(self):
        return self.find_element(self.CONTINUE_BTN)

    def click_continue_recovery_btn(self):
        return self.find_element(self.CONTINUE_BTN).click()

    def find_go_back_to_recovery_page_btn(self):
        return self.find_element(self.GO_BACK_BTN)

    def click_on_go_back_to_recovery_btn(self):
        return self.find_element(self.GO_BACK_BTN).click()

    def find_radio_buttons_on_recovery_method_page(self):
        return self.find_elements(self.RADIO_BUTTONS)

    def find_continue_reset_pwd_btn(self):
        return self.find_element(self.CONTINUE_BTN_2_STAGE)

    def find_cancel_pwd_reset_btn(self):
        return self.find_element(self.CANCEL_RESET_BTN)