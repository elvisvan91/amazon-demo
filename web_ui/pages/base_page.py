"""
@Author: Van.Vo
"""
from selenium.webdriver import ActionChains

from web_ui.libs.custom_log import DEBUG, wait_time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class BasePage(object):
    def __init__(self, driver):
        self.timeout = 10
        self.driver = driver

    def maximize_window(self):
        """
        Maximize the browser window
        """
        self.driver.maximize_window()

    def input_text_by_xpath(self, xpath_locator, text):
        """
        Enter text into the field by xpath
        """
        if self.waiting_for_element_loaded(xpath_locator, By.XPATH):
            DEBUG("Input %s to the %s" % (text, xpath_locator))
            textbox = self.driver.find_element(By.XPATH, xpath_locator)
            textbox.clear()
            textbox.send_keys(text)
        else:
            msg = "Failed to fill '%s' to field %s" % (text, xpath_locator)
            raise Exception(msg)

    def get_element_from_xpath(self, xpath):
        """
        Returns elements locator using xpath.
        """
        return self.driver.find_element_by_xpath(xpath)

    def click_element_by_xpath(self, element):
        """
        Clicks an element by element xpath
        """
        if self.wait_for_element_clickable(element, By.XPATH):
            DEBUG("Click on the element by xpath: %s" % element)
            element = self.driver.find_element(By.XPATH, element)
            element.click()
            wait_time(2)
        else:
            msg = "Element %s is not click-able" % element
            raise Exception(msg)

    def waiting_for_element_loaded(self, condition, By):
        """
        Waits for the element is loaded
        """
        result = False
        try:
            DEBUG("Wait for element %s loaded" % condition)
            wait = WebDriverWait(self.driver, self.timeout)
            element = wait.until(
                EC.presence_of_element_located((By, condition)))
            if element:
                result = True
        except Exception as e:
            DEBUG("Wait for element loaded exception: %s" % e)
        return result

    def wait_for_element_clickable(self, condition, By, timeout=None):
        """
        Waits for the element is clickable
        """
        result = False
        try:
            DEBUG("Wait for element %s click-able" % condition)
            if not timeout:
                timeout = self.timeout
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.element_to_be_clickable((By, condition)))
            if element:
                result = True
        except Exception as err:
            DEBUG("waiting element exception: % s" % err)
        return result

    def waiting_for_element_visible(self, condition, By, timeout=None):
        """
        Waits for the element is visible
        """
        result = False
        try:
            DEBUG("Wait for element %s visible" % condition)
            if not timeout:
                timeout = self.timeout
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(
                EC.visibility_of_element_located((By, condition)))
            if element:
                result = True
        except Exception as err:
            DEBUG("waiting element exception: % s" % err)
        return result

    @staticmethod
    def is_visible(locator):
        """
        Checks if the element is visible on the current page.
        """
        if not locator:
            return False
        return locator.is_displayed()

    def get_text_if_present_by_xpath(self, locator):
        """
        Returns the text of the element if present, None otherwise.
        """
        if not self.waiting_for_element_visible(locator, By.XPATH):
            return None
        return self.get_element_from_xpath(locator).text

    def select_visible_text_by_xpath(self, locator, text):
        """
        Select visible text by xpath
        """
        element = self.get_element_from_xpath(locator)
        select = Select(element)
        select.select_by_visible_text(text)

    def move_mouse(self, locator):
        """
        Move mouse to element
        """
        action = ActionChains(self.driver)
        element = self.get_element_from_xpath(locator)
        move_to_element = action.move_to_element(element)
        move_to_element.click().perform()
