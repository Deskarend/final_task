
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage



def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page=MainPage(browser,link)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link="http://selenium1py.pythonanywhere.com"
    page=MainPage(browser,link)
    page.open()
    page.go_to_basket_page()
    basket_page=BasketPage(browser,browser.current_url)
    basket_page.test_is_basket_empty()
    basket_page.test_is_there_text_empty_basket()




