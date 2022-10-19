from selenium.webdriver.common.by import By

from Orangechrmlive.Src.locators.locators import Locator


class PomLogo(object):
    def __init__(self, driver):
        self.driver = driver

        self.UserNameBar = driver.find_element(By.NAME, Locator.UserNameBar)
        self.PasswordBar = driver.find_element(By.NAME, Locator.PasswordBar)
        self.SignIn_button = driver.find_element(By.CLASS_NAME, Locator.SignIn_button)

    def getUserNameBar(self):
        return self.UserNameBar

    def getPasswordBar(self):
        return self.PasswordBar

    def getSignInButton(self):
        return self.SignIn_button
