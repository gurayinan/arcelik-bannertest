from selenium.webdriver.common.by import By


class ArcelikMainPageLocators(object):
    PROMO_BANNER = (By.CLASS_NAME, "nivo-imageLink")
    ONLINE_SHOP = (By.CLASS_NAME, "onlineSatis")
    PROMOTIONS = (By.CLASS_NAME, "kampanyalar")
    AUTHORIZED_TECH_SERVICE = (By.CLASS_NAME, "modul1")