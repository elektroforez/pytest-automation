from playwright.sync_api import Page, expect


class ProductDetailPage:
    def __init__(self, page: Page):
        self.page = page

        self.__name = self.page.locator(".product-details h2")
        self.__category = self.page.locator('.product-details p:has-text("Category")')
        self.__price = self.page.locator('.product-details:has-text("Rs.")')
        self.__availability = self.page.get_by_text('Availability:')
        self.__condition = self.page.get_by_text('Condition:')
        self.__brand = self.page.get_by_text('Brand:')

    def get_product_name(self):
        return self.__name

    def get_product_category(self):
        return self.__category

    def get_product_price(self):
        return self.__price

    def get_product_availability(self):
        return self.__availability

    def get_product_condition(self):
        return self.__condition

    def get_product_brand(self):
        return self.__brand

    def check_elements_visible(self):
        for locator in [self.__name, self.__category, self.__price, self.__availability, self.__condition,
                        self.__brand]:
            expect(locator).to_be_visible()
