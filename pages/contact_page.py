from playwright.sync_api import Page

class ContactPage:
    def __init__(self, page: Page):
        self.page = page

        self.__name_input = page.locator('input[data-qa="name"]')
        self.__email_input = page.locator('input[data-qa="email"]')
        self.__subject = page.locator('input[data-qa="subject"]')
        self.__message_input = page.locator('textarea[data-qa="message"]')
        self.__file_input = page.locator("input[type=file]")
        self.__submit_btn = page.locator('input[type="submit"]')
        self.__header = page.get_by_text("Get In Touch")
        self.__success_message = page.locator('.contact-form').get_by_text("Success! Your details have been submitted successfully.")
        self.__success_btn = page.locator('a[class="btn btn-success"]')

    def get_header(self):
        return self.__header

    def get_success_message(self):
        return self.__success_message

    def set_name(self, name):
        self.__name_input.fill(name)

    def set_email(self, email: str):
        self.__email_input.fill(email)

    def set_subject(self, subject: str):
        self.__subject.fill(subject)

    def set_message(self, message: str):
        self.__message_input.scroll_into_view_if_needed()
        self.__message_input.fill(message)

    def set_file(self, file: str):
        with self.page.expect_file_chooser() as fc_info:
            self.__file_input.click()
        file_chooser = fc_info.value
        file_chooser.set_files(file)

    def click_submit_btn(self):
        self.__submit_btn.click()


    def click_success_btn(self):
        self.__success_btn.click()

    def fill_contact_form(self, name: str, email: str, subject: str, message: str, file: str):
        self.set_name(name)
        self.set_email(email)
        self.set_subject(subject)
        self.set_message(message)
        self.__message_input.blur()
        self.set_file(file)