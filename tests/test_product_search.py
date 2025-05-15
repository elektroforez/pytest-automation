import allure
import pytest

from playwright.sync_api import expect
from pages.header import Header
from pages.products_page import ProductsPage
from data.fake_input_data import FakeInputData
from pages.product_detail_page import ProductDetailPage
from utils.tools import take_screenshot


class TestProductSearch:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.products_page = ProductsPage(self.page)
        self.header = Header(self.page)
        self.input_data = FakeInputData()
        self.product_detail_page = ProductDetailPage(self.page)

    @allure.title("Test Case 9: Product Search")
    def test_product_search(self, test_setup):
        with allure.step("Verify that home page is visible successfully"):
            expect(self.page).to_have_title('Automation Exercise')

        with allure.step("Click on 'Products' button"):
            self.header.click_products_btn()

        with allure.step("Verify user is navigated to ALL PRODUCTS page successfully"):
            expect(self.page).to_have_title('Automation Exercise - All Products')

        with allure.step("Enter product name in search input and click search button"):
            self.products_page.set_search_input(self.input_data.search_text)
            self.products_page.click_search_btn()

        with allure.step("Verify 'SEARCHED PRODUCTS' is visible"):
            expect(self.products_page.get_title()).to_be_visible()
        take_screenshot(self.page, "test_search_products")

        with allure.step("Verify all the products related to search are visible"):
            self.products_page.check_search_results(self.input_data.search_term)
