import allure
import pytest

from playwright.sync_api import expect

from data.fake_input_data import FakeInputData
from pages.sing_up_page import SingUp
from pages.header import Header
from utils.tools import take_screenshot


class TestSingUp:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.sing_up_page = SingUp(self.page)
        self.header = Header(self.page)
        self.input = FakeInputData()

    @allure.title("Test Case 1: Register User")
    def test_singup(self, test_setup):
        with allure.step("Verify that home page is visible successfully"):
            expect(self.page).to_have_title('Automation Exercise')

        with allure.step("Click on 'Signup / Login' button"):
            self.header.click_login_btn()

        with allure.step("Verify 'New User Signup!' is visible"):
            expect(self.sing_up_page.get_sing_up_title()).to_be_visible()

        with allure.step("Enter name and email address"):
            self.sing_up_page.sing_up(self.input.name, self.input.email)

        with allure.step("Verify that 'ENTER ACCOUNT INFORMATION' is visible"):
            expect(self.sing_up_page.get_create_account_title()).to_be_visible()

        with allure.step("Fill details"):
            self.sing_up_page.fill_in_sing_up_form('mr', self.input.password, self.input.date_day,
                                               self.input.date_month, self.input.date_year, self.input.firstname,
                                               self.input.lastname, self.input.company, self.input.address,
                                               self.input.address2, self.input.country, self.input.state,
                                               self.input.city, self.input.zipcode, self.input.phone)

        with allure.step("Verify that 'ACCOUNT CREATED!' is visible"):
            expect(self.sing_up_page.get_account_created()).to_contain_text("Account Created!")
        take_screenshot(self.page, "test_singup")

        with allure.step("Click 'Continue' button"):
            self.sing_up_page.click_continue_btn()

        with allure.step(" Verify that 'Logged in as username' is visible"):
            expect(self.header.get_logged_in_btn()).to_be_visible()

        with allure.step("Click 'Delete Account' button"):
            self.header.click_delete_account_btn()

        with allure.step("Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button"):
            expect(self.sing_up_page.get_account_deleted()).to_be_visible()
            self.sing_up_page.click_continue_btn()

    @allure.title("Test Case 5: Register User with existing email")
    def test_sing_up_with_existing_email(self, test_setup):
        with allure.step("Verify that home page is visible successfully"):
            expect(self.page).to_have_title('Automation Exercise')

        with allure.step("Click on 'Signup / Login' button"):
            self.header.click_login_btn()

        with allure.step("Verify 'New User Signup!' is visible"):
            expect(self.sing_up_page.get_sing_up_title()).to_be_visible()

        with allure.step("Enter name and already registered email address"):
            self.sing_up_page.sing_up(self.input.name, self.input.existing_email)

        with allure.step("Verify error 'Email Address already exist!' is visible"):
            expect(self.sing_up_page.get_email_error()).to_be_visible()
        take_screenshot(self.page, "test_sing_up_with_existing_email")