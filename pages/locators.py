from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, 'form[id="login_form"]')
    REG_FORM = (By.CSS_SELECTOR, 'form[id="register_form"]')


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, 'button[class="btn btn-lg btn-primary btn-add-to-basket"]')
    ADDING_MESSAGE = (By.CSS_SELECTOR, 'div.alert-success:first-child')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main h1')
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')