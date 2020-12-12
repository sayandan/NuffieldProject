import time
from selenium.webdriver.common.by import By
from PageObjects.BookTour import BookTour
from Utilities.BasePage import BasePage


class GymTour(BasePage):

    """ By_locators  ---  Object Repositories """
    POSTCODE_TEXTBOX = (By.CSS_SELECTOR, 'input.hero-location-finder__input')
    CLOSE_BUTTON = (By.CSS_SELECTOR, 'button.hero-location-finder__close')
    GYM_ADDRESSES_TEXT = (By.CSS_SELECTOR, 'li.grid__cell div.location-finder__address')
    BOOK_GYM_TOUR_BUTTONS = (By.CSS_SELECTOR, 'li.grid__cell a.location-finder__card-action--green')

    """Constructor of the HomePage class"""
    def __init__(self, driver):
        super().__init__(driver)

    """Gym tour actions"""
    def get_gym_addresses(self):
        return self.get_elements(self.GYM_ADDRESSES_TEXT)

    def get_tour_buttons(self):
        return self.get_elements(self.BOOK_GYM_TOUR_BUTTONS)

    def is_close_button_exist(self):
        return self.is_visible(self.CLOSE_BUTTON)

    def book_gym_tour(self):
        print('gym tour')
        buttons = self.get_elements(self.BOOK_GYM_TOUR_BUTTONS)
        print(len(buttons))
        for index, button in enumerate(buttons):
            print('inside for loop')
            print(index)
            if index == 1:
                print(index)
                time.sleep(5)
                button.click()
                #self.do_click(button)
                return BookTour(self.driver)





