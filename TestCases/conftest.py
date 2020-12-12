import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Utilities.TestData import TestData

options = Options()
# disable popups that asked to allow locations etc, pass argument 1 to allow and 2 to block
options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
# disable Chrome info bar that shows its been controlled by test
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option('excludeSwitches', ['enable-logging']) # remove devtools/device errors
options.add_argument("start-maximized")


@pytest.fixture(params=['chrome'], scope='class')
def init_driver(request):
    if request.param == 'chrome':
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH, options=options)
    if request.param == 'edge':
        web_driver = webdriver.Edge(executable_path=TestData.EDGE_EXECUTABLE_PATH)
    web_driver.get(TestData.BASE_URL)
    web_driver.find_element_by_css_selector('a#cookie-banner-close').click()

    # accept cookies and refresh
    # web_driver.add_cookie({'name': 'notice_gdpr_prefs', 'value': '0,1,2:', 'domain':  'nuffieldhealth.com'})
    # web_driver.add_cookie({'name': 'notice_preferences', 'value': '2:', 'domain':  'nuffieldhealth.com'})
    # web_driver.refresh()

    request.cls.driver = web_driver
    # yield
    # web_driver.quit()
