"""
@Author: Van.Vo
"""
import re
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
from web_ui.libs.custom_log import DEBUG
from web_ui.pages.base_page import BasePage
from dateutil.parser import parse


class BaseSearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.search_text_box = "*//input[@id='twotabsearchtextbox']"
        self.submit_search = "*//span[@id='nav-search-submit-text']"
        self.drop_down_sort = "*//select[@id='s-result-sort-select']"
        self.login_page = "//a[@data-nav-role='signin']"
        self.username = "//input[@name='email']"
        self.password = "//input[@name='password']"
        self.continue_btn = "//input[@id='continue']"
        self.submit_btn = "//input[@type='submit']"
        self.card_capacity = "*//div[@id='filters']//*[contains(text(),'%s')]"
        self.item = "//*[@data-cel-widget='search_result_2']//h2"
        self.add_to_cart_btn = "//*[@id='add-to-cart-button']"
        self.cart = "//*[@id='nav-cart']"
        self.quantity_dropdown = "//*[@data-a-class='quantity']"
        self.quantity_number = "//*[@class='a-popover-wrapper']//ul//*[contains(text(), '%s')]"
        self.item_price = "//*[@data-name='Active Items']//p/span"
        self.subtotal = "//*[@data-name='Subtotals']/span[@id='sc-subtotal-amount-activecart']/span"
        self.delete_item = "//span[data-action='delete']/span/input"
        self.empty_cart = "*//h1[contains(text(), 'Your Amazon Cart is empty.')]"

    def input_search_box(self, product_name):
        """
        Input text to search box
        """
        self.input_text_by_xpath(self.search_text_box, product_name)

    def choose_card_capacity(self, capacity):
        """
        Choose card capacity
        """
        self.click_element_by_xpath(self.card_capacity % capacity)

    def click_submit_search(self):
        """
        Click search submit button
        """
        self.click_element_by_xpath(self.submit_search)

    def choose_sort_type(self, sort_type):
        """
        Choose sort type if visible
        """
        self.select_visible_text_by_xpath(self.drop_down_sort, sort_type)

    def go_to_login_page(self):
        """
        Go to login page
        """
        self.click_element_by_xpath(self.login_page)

    def input_username(self, username):
        """
        Input username
        """
        self.input_text_by_xpath(self.username, username)

    def input_password(self, password):
        """
        Input password
        """
        self.input_text_by_xpath(self.password, password)

    def click_continue_btn(self):
        """
        Click continue button
        """
        self.click_element_by_xpath(self.continue_btn)

    def click_submit_btn(self):
        """
        Click submit button
        """
        self.click_element_by_xpath(self.submit_btn)

    def choose_item_on_result_list(self):
        """
        Choose 1 item on result list
        """
        self.click_element_by_xpath(self.item)

    def add_item_to_cart(self):
        """
        Add item to cart
        """
        self.click_element_by_xpath(self.add_to_cart_btn)

    def go_to_cart(self):
        """
        Go to cart
        """
        self.click_element_by_xpath(self.cart)

    def change_quantity_in_cart(self, quantity):
        """
        Choose quantity in cart
        """
        self.click_element_by_xpath(self.quantity_dropdown)
        self.click_element_by_xpath(self.quantity_number % quantity)

    def get_item_price(self):
        """
        Get price of 1 item in cart
        """
        text = self.get_text_if_present_by_xpath(self.item_price)
        item_price = float(text.replace('$', ''))
        return item_price

    def get_subtotal(self):
        """
        Get subtotal of cart
        """
        text = self.get_text_if_present_by_xpath(self.subtotal)
        subtotal = float(text.replace('$', ''))
        return subtotal

    def delete_item_in_cart(self):
        """
        Delete item in cart
        """
        self.click_element_by_xpath("//*[@data-action='delete']/span/input")
        # self.change_quantity_in_cart("0 (Delete)")
