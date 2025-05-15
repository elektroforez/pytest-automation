from playwright.sync_api import Page

class Footer():
    def __init__(self, page: Page):
        self.page = page

        self.__email = self.page.locator('input[type="email"]')
        self.__submit = self.page.locator('button[type="submit"]')
        self.__title = self.page.get_by_text("Subscription")
        self.__success_message = self.page.locator("#success-subscribe")

    def get_title(self):
        return self.__title
    def get_success_message(self):
        return self.__success_message
    def set_email(self, email: str):
        self.__email.fill(email)
    def click_submit(self):
        self.__submit.click()