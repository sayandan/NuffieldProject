from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Utilities.BasePage import BasePage
from Utilities.TestData import TestData


class BookTour(BasePage):

    """By locators"""
    FIRSTNAME_TEXTBOX = (By.ID, 'first_name')
    LASTNAME_TEXTBOX = (By.ID, 'last_name')
    PREFERRED_DAY_SELECT = (By.CSS_SELECTOR, 'select#field-preferred-date-of-visit-day')
    PREFERRED_MONTH_SELECT = (By.CSS_SELECTOR, 'select#field-preferred-date-of-visit-month')
    PREFERRED_YEAR_SELECT = (By.CSS_SELECTOR, 'select#field-preferred-date-of-visit-year')
    PREFERRED_TIME_TEXTBOX = (By.CSS_SELECTOR, 'input#field-preferred-time-of-visit')
    SPECIFIC_GYM_SELECT = (By.CSS_SELECTOR, 'select#gyms-location')
    EMAIL_TEXTBOX = (By.ID, 'email')
    PHONE_TEXTBOX = (By.ID, 'phone')
    MARKETING_PREF_CHECK = (By.CSS_SELECTOR, "label[for='marketing_optin_email']")
    TERMS_CONDITION_CHECK = (By.CSS_SELECTOR, "label[for='terms']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[name=submit]')
    CAPTCHA_ERROR_TEXT = (By.CSS_SELECTOR, 'div#recaptcha_errors ul li')

    """Constructor"""
    def __init__(self, driver):
        super().__init__(driver)

    """actions"""
    def fill_form(self):
        self.do_send_keys(self.FIRSTNAME_TEXTBOX,TestData.FIRSTNAME)
        self.do_send_keys(self.LASTNAME_TEXTBOX,TestData.LASTNAME)
        self.select_drop_down(self.PREFERRED_DAY_SELECT, TestData.PREF_DAY)
        self.select_drop_down(self.PREFERRED_MONTH_SELECT, TestData.PREF_MONTH)
        self.select_drop_down(self.PREFERRED_YEAR_SELECT, TestData.PREF_YEAR)
        self.do_send_keys(self.PREFERRED_TIME_TEXTBOX, TestData.PREF_TIME)
        self.select_drop_down(self.SPECIFIC_GYM_SELECT, TestData.PREF_GYM)
        self.do_send_keys(self.EMAIL_TEXTBOX, TestData.EMAIL)
        self.do_send_keys(self.PHONE_TEXTBOX, TestData.PHONE)
        self.do_click(self.MARKETING_PREF_CHECK)
        self.do_click(self.TERMS_CONDITION_CHECK)
        self.do_click(self.SUBMIT_BUTTON)

    def get_captcha_error(self):
        return self.get_element_text(self.CAPTCHA_ERROR_TEXT)













