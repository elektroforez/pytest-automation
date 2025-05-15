from playwright.sync_api import Page


class SingUp:
    def __init__(self, page: Page):
        self.page = page

        self.__name_input = self.page.locator('input[data-qa="signup-name"]')
        self.__email_input = self.page.locator('input[data-qa="signup-email"]')
        self.__singUp_btn = self.page.locator('button[data-qa="signup-button"]')
        self.__title_mr_radio = self.page.locator('#id_gender1')
        self.__title_ms_radio = self.page.locator('#id_gender2')
        self.__password_input = self.page.locator('input[data-qa="password"]')
        self.__date_day_select = self.page.locator('select[data-qa="days"]')
        self.__date_month_select = self.page.locator('select[data-qa="months"]')
        self.__date_year_select = self.page.locator('select[data-qa="years"]')
        self.__newsletter_checkbox = self.page.locator('#newsletter')
        self.__optin_checkbox = self.page.locator('#optin')
        self.__first_name_input = self.page.locator('input[data-qa="first_name"]')
        self.__last_name_input = self.page.locator('input[data-qa="last_name"]')
        self.__company_input = self.page.locator('input[data-qa="company"]')
        self.__address_input = self.page.locator('input[data-qa="address"]')
        self.__address2_input = self.page.locator('input[data-qa="address2"]')
        self.__country_select = self.page.locator('select[data-qa="country"]')
        self.__state_input = self.page.locator('input[data-qa="state"]')
        self.__city_input = self.page.locator('input[data-qa="city"]')
        self.__zipcode_input = self.page.locator('input[data-qa="zipcode"]')
        self.__mobile_input = self.page.locator('input[data-qa="mobile_number"]')
        self.__sing_up_title = self.page.get_by_text('New User Signup!')
        self.__create_account_btn = self.page.get_by_text("Create Account")
        self.__create_account_title = self.page.get_by_text('Enter Account Information')
        self.__account_created = self.page.locator('h2[data-qa="account-created"]')
        self.__account_deleted = self.page.get_by_text("Account Deleted!")
        self.__continue_btn = self.page.locator('a[data-qa="continue-button"]')
        self.__email_error = self.page.get_by_text("Email Address already exist!")

    def get_sing_up_title(self):
        return self.__sing_up_title

    def get_create_account_title(self):
        return self.__create_account_title

    def get_account_created(self):
        return self.__account_created

    def get_account_deleted(self):
        return self.__account_deleted

    def get_email_error(self):
        return self.__email_error

    def set_name(self, singup_name: str) -> None:
        self.__name_input.fill(singup_name)

    def set_email(self, singup_email: str) -> None:
        self.__email_input.fill(singup_email)

    def set_password(self, singup_password: str) -> None:
        self.__password_input.fill(singup_password)

    def set_date_day_select(self, day: str) -> None:
        self.__date_day_select.scroll_into_view_if_needed()
        self.__date_day_select.select_option(day)

    def set_date_month_select(self, month: str) -> None:
        self.__date_month_select.select_option(month)

    def set_date_year_select(self, year: str) -> None:
        self.__date_year_select.select_option(year)

    def set_newsletter_checkbox(self) -> None:
        self.__newsletter_checkbox.check()

    def set_optin_checkbox(self) -> None:
        self.__optin_checkbox.check()

    def set_first_name_input(self, first_name: str) -> None:
        self.__first_name_input.fill(first_name)

    def set_last_name_input(self, last_name: str) -> None:
        self.__last_name_input.fill(last_name)

    def set_company_input(self, company: str) -> None:
        self.__company_input.fill(company)

    def set_address_input(self, address: str) -> None:
        self.__address_input.fill(address)

    def set_address2_input(self, address2: str) -> None:
        self.__address2_input.fill(address2)

    def set_country_select(self, country: str) -> None:
        self.__country_select.select_option(country)

    def set_state_input(self, state: str) -> None:
        self.__state_input.fill(state)

    def set_city_input(self, city: str) -> None:
        self.__city_input.fill(city)

    def set_zipcode_input(self, zipcode: str) -> None:
        self.__zipcode_input.fill(zipcode)

    def set_mobile_input(self, mobile: str) -> None:
        self.__mobile_input.fill(mobile)

    def click_singup_btn(self) -> None:
        self.__singUp_btn.click()

    def click_create_account_btn(self) -> None:
        self.__create_account_btn.click()

    def click_continue_btn(self) -> None:
        self.__continue_btn.click()

    def sing_up(self, name: str, email: str) -> None:
        self.set_name(name)
        self.set_email(email)
        self.__singUp_btn.click()

    def fill_in_sing_up_form(self, title: str, password: str, date_day: str, date_month: str, date_year: str,
                             first_name: str, last_name: str, company: str, address: str, address2: str, country: str,
                             state: str, city: str, zipcode: str, number: str) -> None:
        self.__title_mr_radio.click()
        self.set_password(password)
        self.set_date_day_select(date_day)
        self.set_date_month_select(date_month)
        self.set_date_year_select(date_year)
        self.set_newsletter_checkbox()
        self.set_optin_checkbox()
        self.set_first_name_input(first_name)
        self.set_last_name_input(last_name)
        self.set_company_input(company)
        self.set_address_input(address)
        self.set_address2_input(address2)
        self.set_country_select(country)
        self.set_state_input(state)
        self.set_city_input(city)
        self.set_zipcode_input(zipcode)
        self.set_mobile_input(number)
        self.click_create_account_btn()

