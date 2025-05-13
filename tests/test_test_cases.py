import allure
import pytest

from playwright.sync_api import expect
from pages.header import Header

class TestTestCasesPage:
    @pytest.fixture()
    def test_setup(self, new_page):
        self.page = new_page
        self.header = Header(self.page)

    @allure.title("Test Case 7: Verify Test Cases Page")
    def test_test_cases_page(self, test_setup, base_url):
        with allure.step("Verify that home page is visible successfully"):
            expect(self.page).to_have_title('Automation Exercise')

        with allure.step("Click on 'Test Cases' button"):
            self.header.click_test_cases_btn()

        with allure.step("Verify user is navigated to test cases page successfully"):
            expect(self.page).to_have_url(base_url + '/test_cases')