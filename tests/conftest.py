# import allure
import pytest

from playwright.sync_api import Playwright
from pages.sing_up_page import SingUp
from pages.header import Header
from utils.dialog_consent import DialogConsent
from data.fake_input_data import FakeInputData

BASE_URL = "https://www.automationexercise.com"
disable_loggers = []

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture
def new_page(playwright: Playwright, request):
    browser_name = request.config.getoption('--browser_name')
    headless = False if request.config.getoption("--headed") else True
    if browser_name == "chromium":
        browser = playwright.chromium.launch(headless=headless)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=headless)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=headless)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://www.automationexercise.com/')
    contest = DialogConsent(page)
    contest.accept()
    yield page
    browser.close()

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chromium')

@pytest.fixture
def register_user(new_page):
    page = new_page
    header = Header(page)
    signup = SingUp(page)
    input_data = FakeInputData()

    user_name = input_data.name
    email = input_data.email
    password = input_data.password
    day = input_data.date_day
    month = input_data.date_month
    year = input_data.date_year

    header.click_login_btn()
    signup.sing_up(user_name, email)
    signup.fill_in_sing_up_form('mr',password, day, month, year, input_data.firstname,
                                               input_data.lastname, input_data.company, input_data.address,
                                               input_data.address2, input_data.country, input_data.state,
                                               input_data.city, input_data.zipcode, input_data.phone)
    signup.click_continue_btn()
    header.click_logout_btn()
    page.goto(BASE_URL)

    return email, password, user_name