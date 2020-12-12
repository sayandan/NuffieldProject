from PageObjects.BookTour import BookTour
from PageObjects.HomePage import HomePage
from Utilities.BaseTest import BaseTest
from Utilities.TestData import TestData


class TestGymTour(BaseTest):

    def test_05_close_button(self):
        self.homepage = HomePage(self.driver)
        self.gym_tour = self.homepage.search_nearest_gym(TestData.POSTCODE)
        assert self.gym_tour.is_close_button_exist()

    def test_06_gym_addresses(self):
        self.homepage = HomePage(self.driver)
        self.gym_tour = self.homepage.search_nearest_gym(TestData.POSTCODE)
        addresses = self.gym_tour.get_gym_addresses()
        for index, address in enumerate(addresses):
            print(index, address.text)
            if index == 0:
                assert TestData.NEAREST_GYM_POSTCODE in address.text

    # def test_07_gym_tour(self):
    #     self.homepage = HomePage(self.driver)
    #     self.gym_tour = self.homepage.search_nearest_gym(TestData.POSTCODE)
    #     self.gym_tour.book_gym_tour()

    def test_08_form(self):
        self.homepage = HomePage(self.driver)
        print('homepage created')
        self.gym_tour = self.homepage.search_nearest_gym(TestData.POSTCODE)
        print('gym tour created')
        self.book_tour = self.gym_tour.book_gym_tour()
        self.book_tour.fill_form()
        assert self.book_tour.get_captcha_error() == TestData.CAPTCHA_ERROR

