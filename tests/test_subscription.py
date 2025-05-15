import allure
import pytest

from playwright.sync_api import expect

from pages.footer import Footer
from data.fake_input_data import FakeInputData

class TestSubscription:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.footer = Footer(self.page)
        self.input_data = FakeInputData()

    @allure.title("Test Case 10: Verify Subscription in home page")
    def test_subscription(self, test_setup):
        with allure.step("Verify that home page is visible successfully"):
            expect(self.page).to_have_title('Automation Exercise')

        with allure.step("Enter email address in input and click arrow button"):
            self.footer.set_email(self.input_data.existing_email)
            self.footer.click_submit()

        with allure.step("Verify success message 'You have been successfully subscribed!' is visible"):
            expect(self.footer.get_success_message()).to_be_visible()
