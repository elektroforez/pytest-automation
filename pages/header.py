from playwright.sync_api import Page


class Header():
    def __init__(self, page: Page):
        self.page = page

        self.__logout_btn = self.page.locator("a[href='/logout']")
        self.__login_btn = self.page.locator("a[href='/login']")
        self.__test_cases_btn = self.page.locator(".navbar-nav a[href='/test_cases']")
        self.__products_btn = self.page.locator("a[href='/products']")
        self.__delete_account_btn = self.page.locator('a[href="/delete_account"]')
        self.__logged_in_btn = self.page.get_by_text("Logged in")
        self.__contact_us_btn = self.page.locator('a[href="/contact_us"]')

    def get_logged_in_btn(self):
        return self.__logged_in_btn

    def click_logout_btn(self):
        self.__logout_btn.click()

    def click_login_btn(self):
        self.__login_btn.click()

    def click_test_cases_btn(self):
        self.__test_cases_btn.click()

    def click_products_btn(self):
        self.__products_btn.click()

    def click_delete_account_btn(self):
        self.__delete_account_btn.click()

    def click_contact_us_btn(self):
        self.__contact_us_btn.click()