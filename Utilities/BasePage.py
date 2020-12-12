from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from Utilities.TestData import TestData

"""This class is the parent of all pages"""
"""It contains all the generic methods and utilities for all the pages"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 1).until(ec.presence_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(by_locator)).clear()
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        return WebDriverWait(self.driver, 1).until(ec.presence_of_element_located(by_locator)).text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 1).until(ec.visibility_of_element_located(by_locator))
        return bool(element)

    def get_elements(self, by_locator):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located(by_locator))

    def get_title(self, title):
        WebDriverWait(self.driver, 1).until(ec.title_is(title))
        return self.driver.title

    def press_enter_key(self, by_locator):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(by_locator)).send_keys(Keys.RETURN)

    def select_drop_down(self, by_locator, text):
        select = Select(self.driver.find_element(*by_locator))
        select.select_by_visible_text(text)


