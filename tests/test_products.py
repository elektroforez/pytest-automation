import allure
import pytest

from playwright.sync_api import expect
from pages.header import Header
from pages.products_page import ProductsPage
from pages.product_detail_page import ProductDetailPage
from utils.tools import take_screenshot


class TestProducts:
    @pytest.fixture()
    def test_setup(self, new_page):
        self.page = new_page
        self.products_page = ProductsPage(self.page)
        self.header = Header(self.page)
        self.product_detail_page = ProductDetailPage(self.page)

    @allure.title("Test Case 8: Verify All Products and product detail page")
    def test_product_details_page(self, test_setup, base_url):
        with allure.step("Verify that home page is visible successfully"):
            expect(self.page).to_have_title('Automation Exercise')

        with allure.step("Click on 'Products' button"):
            self.header.click_products_btn()

        with allure.step("Verify user is navigated to ALL PRODUCTS page successfully"):
            expect(self.page).to_have_title('Automation Exercise - All Products')

        with allure.step("The products list is visible"):
            expect(self.products_page.get_product_list()).to_be_visible()

        with allure.step("Click on 'View Product' of first product"):
            self.products_page.click_view_first_product()

        with allure.step("User is landed to product detail page"):
            expect(self.page).to_have_url(base_url + '/product_details/1')
        take_screenshot(self.page, "test_product_details_page_attributes_visible")

        with allure.step("Verify that detail detail is visible: product name, category, price, availability, condition, brand"):
            self.product_detail_page.check_elements_visible()
