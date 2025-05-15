import allure
import pytest

from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.header import Header
from data.fake_input_data import FakeInputData
from utils.tools import take_screenshot


class TestLoginPage:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.login_page = LoginPage(self.page)
        self.header = Header(self.page)
        self.input = FakeInputData()

    @allure.title("Test Case 2: Login User with correct email and password")
    def test_login(self, test_setup, register_user):
        email, password, user_name = register_user
        with allure.step(' Verify that home page is visible successfully'):
            expect(self.page).to_have_title('Automation Exercise')

        with allure.step("Click on 'Signup / Login' button"):
            self.header.click_login_btn()

        with allure.step("Verify 'Login to your account' is visible"):
            expect(self.login_page.get_login_title()).to_be_visible()

        with allure.step("Enter correct email address and password"):
            self.login_page.login(email, password)

        with allure.step("Verify that 'Logged in as username' is visible"):
            expect(self.header.get_logged_in_btn()).to_contain_text(user_name)

        with allure.step("Click 'Delete Account' button"):
            self.header.click_delete_account_btn()

        with allure.step("Verify that 'ACCOUNT DELETED!' is visible"):
            expect(self.login_page.get_form()).to_contain_text("Account Deleted!")

        take_screenshot(self.page, "test_login_account_deleted")

    @allure.title("Test Case 3: Login User with incorrect email and password")
    def test_invalid_login(self, test_setup):
        with allure.step(' Verify that home page is visible successfully'):
            expect(self.page).to_have_title('Automation Exercise')
        with allure.step("Click on 'Signup / Login' button"):
            self.header.click_login_btn()
        with allure.step("Verify 'Login to your account' is visible"):
            expect(self.login_page.get_login_title()).to_be_visible()
        with allure.step("Enter incorrect email address and password"):
            self.login_page.login(self.input.email, self.input.password)
        with allure.step("Verify error 'Your email or password is incorrect!' is visible"):
            expect(self.login_page.get_login_error()).to_be_visible()
        take_screenshot(self.page, "test_login_error")

    @allure.title("Test Case 4: Logout User")
    def test_logout(self, test_setup, base_url, register_user):
        email, password, user_name = register_user
        with allure.step(' Verify that home page is visible successfully'):
            expect(self.page).to_have_title('Automation Exercise')
        with allure.step("Click on 'Signup / Login' button"):
            self.header.click_login_btn()
        with allure.step("Verify 'Login to your account' is visible"):
            expect(self.login_page.get_login_title()).to_be_visible()
        with allure.step("Enter correct email address and password"):
            self.login_page.login(email, password)
        with allure.step("Verify that 'Logged in as username' is visible"):
            expect(self.header.get_logged_in_btn()).to_contain_text(user_name)
        take_screenshot(self.page, "test_logout")
        with allure.step("Click 'Logout' button"):
            self.header.click_logout_btn()
        with allure.step("Verify that user is navigated to login page"):
            expect(self.page).to_have_url(base_url + "/login")