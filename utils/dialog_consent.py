from playwright.sync_api import Page

class DialogConsent():
    def __init__(self, page: Page):
        self.page = page

        self.__accept_button = self.page.locator("button:has-text('Consent')")

    def get_accept_button(self):
        return self.__accept_button
    def accept(self):
        self.__accept_button.click()