from playwright.sync_api import Page

class LoginPage():
    def __init__(self, page: Page):
        self.page = page

        self.__email_input = self.page.locator('input[data-qa="login-email"]')
        self.__password_input = self.page.locator('input[data-qa="login-password"]')
        self.__login_btn = self.page.locator('button[data-qa="login-button"]')
        self.__login_error = self.page.get_by_text("Your email or password is incorrect!")
        self.__login_title = self.page.get_by_text("Login to your account")
        self.__form = self.page.locator('#form')

    def set_email(self, email: str):
        self.__email_input.fill(email)

    def set_password(self, password: str):
        self.__password_input.fill(password)

    def get_login_error(self):
        return self.__login_error

    def get_login_title(self):
        return self.__login_title

    def get_form(self):
        return self.__form

    def click_login(self):
        self.__login_btn.click()

    def login(self, email: str, password: str):
        self.set_email(email)
        self.set_password(password)
        self.click_login()

