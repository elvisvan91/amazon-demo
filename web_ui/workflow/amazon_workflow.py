"""
@Author: Van.Vo
"""
from selenium.webdriver.common.by import By
from web_ui.libs.custom_log import INFO
from web_ui.pages.amazon import BaseSearchPage


class AmazonWorkflow(BaseSearchPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.amazon_wf = BaseSearchPage(self.driver)

    def login_to_amazon(self, username, password):
        """
        Logon to Amazon
        """
        INFO("Go to login page")
        self.amazon_wf.go_to_login_page()
        INFO("Input username")
        self.input_username(username=username)
        INFO("Click continue button")
        self.click_continue_btn()
        INFO("Input password")
        self.input_password(password=password)
        INFO("Click submit button")
        self.click_submit_btn()

    def search_product(self, **kwargs):
        """
        Search department book and language
        """
        keyword = kwargs.get('keyword')
        capacity = kwargs.get('capacity', '64 GB')
        sort = kwargs.get('sort', False)
        sort_type = kwargs.get('sort_type', 'Featured')

        INFO("Input product name")
        self.amazon_wf.input_search_box(keyword)

        INFO("Click submit search button")
        self.amazon_wf.click_submit_search()

        INFO("Choose capacity")
        if capacity:
            self.amazon_wf.choose_card_capacity(capacity)

        INFO("Sorting search result")
        if sort:
            self.amazon_wf.choose_sort_type(sort_type)

    def change_quantity_in_cart(self, quantity=1):
        """
        Change quantity in cart
        """
        INFO("Change quantity")
        self.amazon_wf.change_quantity_in_cart(quantity=quantity)

    def pick_item_and_add_to_cart(self):
        """
        Pick item in result list then add to cart
        """
        INFO("Pick item")
        self.amazon_wf.choose_item_on_result_list()
        INFO("Add to cart")
        self.amazon_wf.add_item_to_cart()
        INFO("Go to cart")
        self.amazon_wf.go_to_cart()

    def verify_subtotal_correct(self, item_quantity):
        """
        Verify subtotal
        """
        INFO("Get price of 1 item")
        item_price = self.amazon_wf.get_item_price()
        INFO("Get subtotal")
        subtotal = self.amazon_wf.get_subtotal()
        INFO("Verify subtotal")
        if subtotal == item_price * item_quantity:
            return True
        return False

    def verify_cart_empty(self):
        """
        Verify cart empty
        """
        INFO("Delete item in cart")
        self.amazon_wf.delete_item_in_cart()
        INFO("Check cart empty")
        if self.waiting_for_element_visible(self.empty_cart, By.XPATH):
            return True
        return False
