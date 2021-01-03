"""
@Author: Van.Vo
"""
from selenium import webdriver
from web_ui.libs.custom_log import DEBUG


class WebDriverFactory(object):

    def __init__(self, browser):
        """
        Init WebDriverFactory class
        """
        self.browser = browser

    def get_web_driver_instance(self, base_url):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            WebDriver Instance
        """
        if self.browser == "firefox" or self.browser == 'ff':
            driver = webdriver.Firefox()
        elif self.browser == "chrome" or self.browser == 'gc':
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Chrome()
        DEBUG("Set implicitly wait to 1.")
        driver.implicitly_wait(1)
        driver.maximize_window()
        driver.delete_all_cookies()
        driver.get(base_url)
        return driver
