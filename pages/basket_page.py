from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def test_is_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_TO_BUY),\
        "basket is not empty"


    def test_is_there_text_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_EMPTY_BASKET),\
        "no text 'basket is empty'"

