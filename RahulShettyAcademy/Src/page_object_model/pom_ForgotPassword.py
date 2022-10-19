from selenium.webdriver.common.by import By
from RahulShettyAcademy.Src.locators.locators import Locator


class ForgotPassword(object):
    def __init__(self, driver):
        self.driver = driver

        self.NameBar = driver.find_element(By.XPATH, Locator.NameBar)
        self.EmailBar = driver.find_element(By.XPATH, Locator.EmailBar)
        self.PhoneNumberBar = driver.find_element(By.CSS_SELECTOR, Locator.PhoneNumberBar)
        self.ResetButton = driver.find_element(By.CSS_SELECTOR, Locator.ResetButton)
        self.PickPass = driver.find_element(By.CSS_SELECTOR, Locator.PickPass)
        self.GoToLoginButton = driver.find_element(By.CSS_SELECTOR, Locator.GoToLoginButton)

    def getNameBar(self):
        return self.NameBar

    def getEmailBar(self):
        return self.EmailBar

    def getPhoneNumberBar(self):
        return self.PhoneNumberBar

    def getResetButton(self):
        return self.ResetButton

    def getPass(self):
        return self.PickPass

    def getGoToLoginButton(self):
        return self.GoToLoginButton
