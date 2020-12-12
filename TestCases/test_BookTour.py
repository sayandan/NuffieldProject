from PageObjects.GymTour import GymTour
from PageObjects.HomePage import HomePage
from Utilities.BaseTest import BaseTest
from Utilities.TestData import TestData


class TestBookTour(BaseTest):

    def test_08_form(self):
        self.homepage = HomePage(self.driver)
        print('homepage created')
        self.gym_tour = self.homepage.search_nearest_gym(TestData.POSTCODE)
        print('gym tour created')
        self.book_tour = self.gym_tour.book_gym_tour()
        self.book_tour.fill_form()
        assert self.book_tour.get_captcha_error() == TestData.CAPTCHA_ERROR



