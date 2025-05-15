from playwright.sync_api import Page, expect

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page

        self.__product_list = page.locator(".features_items")
        self.__view_first_product_btn = page.locator('a[href="/product_details/1"]')
        self.__search_input = page.locator('input[name="search"]')
        self.__search_btn = page.locator('button[id="submit_search"]')
        self.__title = page.get_by_text('Searched Products')

    def get_product_list(self):
        return self.__product_list

    def get_title(self):
        return self.__title

    def click_view_first_product(self):
        self.__view_first_product_btn.click()

    def set_search_input(self, search_input):
        self.__search_input.fill(search_input)

    def click_search_btn(self):
        self.__search_btn.click()

    def check_search_results(self, search_term: str):
        for i in range(self.__product_list.locator('.productinfo.text-center p').count()):
            expect(self.__product_list.locator('.productinfo.text-center p').nth(i)).to_contain_text(search_term)
