from selenium.webdriver.common.by import By
from RahulShettyAcademy.Src.locators.locators import Locator


class PomLogin(object):
    def __init__(self, driver):
        self.driver = driver

        self.UserNameBar = driver.find_element(By.ID, Locator.UserNameBar)
        self.PasswordBar = driver.find_element(By.NAME, Locator.PasswordBar)
        self.SingInButton = driver.find_element(By.CLASS_NAME, Locator.signinButton)
        self.ForgotYourPassword = driver.find_element(By.LINK_TEXT, Locator.ForgotYourPassword)

    def getUserNameBar(self):
        return self.UserNameBar

    def getPasswordBar(self):
        return self.PasswordBar

    def getSignInButton(self):
        return self.SingInButton

    def grtForgotYourPassword(self):
        return self.ForgotYourPassword
