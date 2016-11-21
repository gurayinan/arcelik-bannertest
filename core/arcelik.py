# -*- coding: utf-8 -*-
from modules import *


class Core(object):

    def __init__(self):
        self.settings_location = os.path.join(os.getcwd(), 'core', 'settings.ini')
        self.settings = {}
        self.import_settings()
        self.driver = None
        self.select_browser()
        self.wait = WebDriverWait(self.driver, 30)

    def import_settings(self):
        try:
            settings = ConfigParser.ConfigParser()
            settings.read(self.settings_location)
            for section in settings.sections():
                for option in settings.options(section):
                    self.settings[option] = settings.get(section, option)
        except StandardError:
            raise

    def chrome_driver(self):
        try:
            if self.settings is not None:
                self.driver = webdriver.Chrome(self.settings.get('chromedriver_path'))
                width = self.driver.execute_script("return window.screen.availWidth")
                height = self.driver.execute_script("return window.screen.availHeight")
                self.driver.set_window_position(0, 0)
                self.driver.set_window_size(width, height)
        except StandardError:
            raise

    def firefox_driver(self):
        try:
            if self.settings is not None:
                self.driver = webdriver.Firefox(self.settings.get('geckodriver_path'))
                self.driver.maximize_window()
        except StandardError:
            raise

    def select_browser(self):
        try:
            if self.settings is not None:
                desired_browser = self.settings.get('desired_browser')
                if desired_browser == "chrome":
                    self.chrome_driver()
                elif desired_browser == "firefox":
                    self.firefox_driver()
                else:
                    print "Desired browser is not available."
                    exit()
        except StandardError:
            raise


class MainPage(Core):

    def check_main_banner(self):
        expected_target = self.driver.execute_script("return $('.nivo-imageLink').attr('href')")
        self.wait.until(ec.element_to_be_clickable(ArcelikMainPageLocators.PROMO_BANNER)).click()
        return expected_target

    def check_online_shop(self):
        expected_target = self.driver.execute_script("return $('.onlineSatis a').attr('href')")
        target = self.driver.find_element_by_link_text('Online Satış')
        target.click()
        return expected_target

    def check_auth_tech_service(self):
        expected_target = self.driver.execute_script("return $('.modul1 a').attr('href')")
        self.wait.until(ec.element_to_be_clickable(ArcelikMainPageLocators.AUTHORIZED_TECH_SERVICE)).click()
        return expected_target

    def check_promotions(self):
        expected_target = self.driver.execute_script("return $('.kampanyalar a').attr('href')")
        target = self.driver.find_element_by_link_text('Kampanyalar')
        target.click()
        return expected_target

