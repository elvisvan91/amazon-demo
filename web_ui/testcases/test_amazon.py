"""
@Author: Van.Vo
"""
import unittest
import pytest
from ddt import ddt
from web_ui.libs.custom_log import STEP, TESTCASE, assert_true
from web_ui.workflow.amazon_workflow import AmazonWorkflow
from web_ui.workflow.ui_constants import USERNAME, PASSWORD


@pytest.mark.usefixtures("setup")
@ddt
class TestSearchPage(unittest.TestCase):
    """
    Testcases for search product on amazon.
    """
    test_data = {
        "keyword": "sd card",
        "capacity": "64 GB",
        "sort_type": "Price: High to Low",
        "quantity": 3
    }

    @pytest.fixture(autouse=True)
    def setUpTest(self, setup):
        """
        Setup for test
        """
        TESTCASE("### RUNNING TEST: " + self.id())
        self.amazon = AmazonWorkflow(self.driver)

    def test_amazon(self):
        """
        Verify result list can be sorted on demand
        """
        STEP("Login into amazon.com")
        self.amazon.login_to_amazon(USERNAME, PASSWORD)

        STEP("Search for item “sd card” with filter [capacity 64 GB] [sort by: price from high to low]")
        self.amazon.search_product(keyword=self.test_data['keyword'],
                                   capacity=self.test_data['capacity'],
                                   sort_type=self.test_data['sort_type'],
                                   sort=True)

        STEP("Pick the item in the list and go to cart")
        self.amazon.pick_item_and_add_to_cart()

        STEP("View the cart, increase quantity to 3")
        self.amazon.change_quantity_in_cart(quantity=self.test_data['quantity'])

        STEP("Verify the subtotal price is correct")
        result_subtotal = self.amazon.verify_subtotal_correct(self.test_data['quantity'])
        assert_true(result_subtotal, "Subtotal is not correct", "Subtotal is correct")

        STEP("Delete the 'sd card' item and verify that the cart is empty")
        result_empty_cart = self.amazon.verify_cart_empty()
        assert_true(result_empty_cart, "FAIL cart is not  empty", "Cart is empty")
