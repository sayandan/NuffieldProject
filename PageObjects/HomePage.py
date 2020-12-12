import time
from selenium.webdriver.common.by import By
from PageObjects.GymTour import GymTour
from Utilities.TestData import TestData
from Utilities.BasePage import BasePage


class HomePage(BasePage):
    """ By_locators  ---  Object Repositories """
    POSTCODE_TEXTBOX = (By.CSS_SELECTOR, 'input.hero-location-finder__input')
    LOGIN_ICON = (By.CSS_SELECTOR, 'i.icon-user')
    FIND_GYM_TEXT = (By.CSS_SELECTOR, 'label.hero-location-finder__label')

    """Constructor of the HomePage class"""
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(TestData.BASE_URL)

    """HomePage actions"""
    def get_homepage_title(self, title):
        return self.get_title(title)

    def is_login_button_exist(self):
        return self.is_visible(self.LOGIN_ICON)

    def get_find_gym_text(self):
        return self.get_element_text(self.FIND_GYM_TEXT)

    def search_nearest_gym(self, postcode):
        self.do_send_keys(self.POSTCODE_TEXTBOX, postcode)
        #action_chain = ActionChains(self.driver)
        #action_chain.send_keys_to_element(self.driver.find_element(*self.POSTCODE_TEXT), postcode + '\n').perform()
        #self.do_send_keys(self.POSTCODE_TEXT, u'\ue007')
        #self.do_send_keys(self.POSTCODE_TEXT, Keys.ENTER)
        time.sleep(6)
        self.press_enter_key(self.POSTCODE_TEXTBOX)
        return GymTour(self.driver)  # this will return GymTour class object














