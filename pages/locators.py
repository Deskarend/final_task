from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM=(By.CSS_SELECTOR,"#login_form")
    LOGIN_REGISTER_FORM=(By.CSS_SELECTOR,"#register_form")
    EMAIL_IN_REGISTER=(By.CSS_SELECTOR,"[name='registration-email']")
    PASSWORD_IN_REGISTER=(By.CSS_SELECTOR,"[name='registration-password1']")
    CONFIRM_PASSWORD_IN_REGISTER=(By.CSS_SELECTOR,"[name='registration-password2']")
    REGISTER_BUTTON=(By.CSS_SELECTOR,"[name='registration_submit']")



class ProductPageLocators():
    ADD_TO_BASKET=(By.CSS_SELECTOR,".btn-add-to-basket")
    MAIN_PRODUCT=(By.CSS_SELECTOR,".product_main >h1")
    ADDED_PRODUCT=(By.CSS_SELECTOR,".alertinner >strong")
    PRODUCT_PRICE=(By.CSS_SELECTOR,"p.price_color")
    BASKET_PRICE=(By.CSS_SELECTOR,".in div > p:nth-child(1) > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")

class BasketPageLocators():
    BASKET=(By.CSS_SELECTOR,".pull-right.hidden-xs > span > a")
    ITEMS_TO_BUY=(By.CSS_SELECTOR,"h2.col-sm-6 ")
    TEXT_EMPTY_BASKET=(By.CSS_SELECTOR,'#content_inner > p')