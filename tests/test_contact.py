import allure
import pytest

from playwright.sync_api import expect
from pages.header import Header
from pages.contact_page import ContactPage
from data.fake_input_data import FakeInputData
from utils.tools import take_screenshot


class TestContact:
    @pytest.fixture()
    def test_setup(self, new_page):
        self.page = new_page
        self.contact_page = ContactPage(self.page)
        self.header = Header(self.page)
        self.input_data = FakeInputData()

    @allure.title("Test Case 6: Contact Us Form")
    def test_contact_form(self, test_setup):
        with allure.step("Verify that home page is visible successfully"):
            expect(self.page).to_have_title('Automation Exercise')
        with allure.step("Click on 'Contact Us' button"):
            self.header.click_contact_us_btn()
        with allure.step("Verify 'GET IN TOUCH' is visible"):
            expect(self.contact_page.get_header()).to_be_visible()
        with allure.step("Fill contact form"):
            self.contact_page.fill_contact_form(self.input_data.name, self.input_data.existing_email, self.input_data.sentence,
                                            self.input_data.sentence, self.input_data.file)
        self.page.on("dialog", lambda dialog: dialog.accept())
        with allure.step("Click 'Submit' button"):
            self.contact_page.click_submit_btn()
        with allure.step("Verify success message 'Success! Your details have been submitted successfully.' is visible"):
            expect(self.contact_page.get_success_message()).to_be_visible()
        take_screenshot(self.page, "test_contact_form")
        with allure.step("Click 'Home' button and verify that landed to home page successfully"):
            self.contact_page.click_success_btn()
            expect(self.page).to_have_title('Automation Exercise')