import time
import pytest
from pages.locators import ProductPageLocators
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage


from .pages.product_page import ProductPage

'''@pytest.mark.parametrize('link', [
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offe7r",marks=pytest.mark.xfail),
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser,link):
    page=ProductPage(browser,link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.is_product_added()
    page.is_corrected_price()
    

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    page=ProductPage(browser,link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    page = ProductPage(browser, link)
    page.open()
    page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)
    

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()'''

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link="http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.test_is_basket_empty()
    basket_page.test_is_there_text_empty_basket()









