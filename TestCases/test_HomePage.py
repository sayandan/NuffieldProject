from PageObjects.HomePage import HomePage
from Utilities.BaseTest import BaseTest
from Utilities.TestData import TestData


class TestHome(BaseTest):

    def test_01_homepage_title(self):
        self.homepage = HomePage(self.driver)
        title = self.homepage.get_title(TestData.PAGE_TITLE)
        assert title == TestData.PAGE_TITLE

    def test_02_login_button(self):
        self.homepage = HomePage(self.driver)
        assert self.homepage.is_login_button_exist()

    def test_03_gym_text(self):
        self.homepage = HomePage(self.driver)
        assert self.homepage.get_find_gym_text() == TestData.FIND_GYM_TEXT

    def test_04_postcode_search(self):
        self.homepage = HomePage(self.driver)
        self.homepage.search_nearest_gym(TestData.POSTCODE)










