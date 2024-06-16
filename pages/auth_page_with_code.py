from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AuthWithCodePage(BasePage):
    INPUT_PHONE_EMAIL = (By.ID, 'address')
    SEND_CODE_BTN = (By.ID, 'otp_get_code')
    CARD_DESCRIPTION = (By.ID, 'card-description')
    INPUT_ALERT = (By.ID, 'address-meta')

    CODE_FORM_TITLE = (By.ID, 'card-title')
    CODE_FORM_DESCRIPTION = (By.ID, 'otp-code-form-description')
    CHANGE_EMAIL_LINK_CODE = (By.ID, 'otp-back')
    CODE_INPUT_FIELDS = (By.XPATH, '//input[@class="rt-input__input rt-sdi-container__input code-input__input rt-input__input--rounded rt-input__input--orange"]')
    TIMEOUT_CODE_RESEND = (By.ID, 'otp-code-timeout')

    TIMEOUT_CODE_RESEND_AUTH_FORM = (By.XPATH, '//div[@class="otp-form__timeout"]')

    CAPTCHA_IMAGE = (By.XPATH, '//div[@class="rt-captcha__image"]')

    def find_card_description_text(self):
        return self.find_element(self.CARD_DESCRIPTION).text

    def find_input_field_for_code_auth(self):
        return self.find_element(self.INPUT_PHONE_EMAIL)

    def fill_input_field_for_code_auth(self, value):
        return self.find_element(self.INPUT_PHONE_EMAIL).send_keys(value)

    def find_send_code_button_auth(self):
        return self.find_element(self.SEND_CODE_BTN)

    def click_on_send_code_button_auth(self):
        return self.find_element(self.SEND_CODE_BTN).click()

    def find_input_error_alert_text(self):
        return self.find_element(self.INPUT_ALERT).text

    def find_email_in_code_form_description_text(self):
        return self.find_element(self.CODE_FORM_DESCRIPTION).text

    def find_change_email_link_in_code_form(self):
        return self.find_element(self.CHANGE_EMAIL_LINK_CODE).text

    def click_change_email_link_in_code_form(self):
        return self.find_element(self.CHANGE_EMAIL_LINK_CODE).click()

    def count_code_input_fields(self):
        return len(self.find_elements(self.CODE_INPUT_FIELDS))

    def check_code_input_fields_take_only_nums(self):
        if self.count_code_input_fields() == 6:
            num_1 = self.find_elements(self.CODE_INPUT_FIELDS)[0].get_attribute('inputMode')
            num_2 = self.find_elements(self.CODE_INPUT_FIELDS)[1].get_attribute('inputMode')
            num_3 = self.find_elements(self.CODE_INPUT_FIELDS)[2].get_attribute('inputMode')
            num_4 = self.find_elements(self.CODE_INPUT_FIELDS)[3].get_attribute('inputMode')
            num_5 = self.find_elements(self.CODE_INPUT_FIELDS)[4].get_attribute('inputMode')
            num_6 = self.find_elements(self.CODE_INPUT_FIELDS)[5].get_attribute('inputMode')
            code_input_fields = [num_1, num_2, num_3, num_4, num_5, num_6]
            return code_input_fields
        else:
            return "Элементы не найдены или у них нет атрибура 'inputMode'."

    def find_code_form_title_text(self):
        return self.find_element(self.CODE_FORM_TITLE).text

    def find_timeout_code_resend_alert_in_auth_form(self):
        return self.find_element(self.TIMEOUT_CODE_RESEND_AUTH_FORM).text

    def find_captcha_image_on_auth_with_code_page(self):
        return self.find_element(self.CAPTCHA_IMAGE)
