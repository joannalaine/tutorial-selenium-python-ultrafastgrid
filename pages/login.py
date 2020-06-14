# Source: https://testautomationu.applitools.com/selenium-webdriver-python-tutorial/chapter4.html
"""
This module contains LoginPage,
the page object for the Applitools Demo login page.
"""
from selenium.webdriver.common.by import By


class LoginPage:
    LOGIN_BUTTON = (By.ID, "log-in")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def load(self):
        self.driver.get(self.url)

    def log_in(self):
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        login_button.click()
