from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        button_add_to_basket=self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button_add_to_basket.click()

    def is_product_added(self):
        product=self.browser.find_element(*ProductPageLocators.MAIN_PRODUCT)
        added_product=self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT)
        assert product.text==added_product.text,"added product is not corrected"

    def is_corrected_price(self):
        product_price=self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        basket_price=self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        assert basket_price.text==product_price.text,\
            "The price of the cart from does not match the price of the product"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True
