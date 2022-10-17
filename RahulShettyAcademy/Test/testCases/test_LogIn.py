import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from Selenium_based_mini_projects_using_Python.RahulShettyAcademy.Src.locators.locators import Locator
from Selenium_based_mini_projects_using_Python.RahulShettyAcademy.Src.base.environment_setup import EnvironmentSetup
from Selenium_based_mini_projects_using_Python.RahulShettyAcademy.Src.page_object_model.pom_logIn_page import PomLogin
from Selenium_based_mini_projects_using_Python.RahulShettyAcademy.Src.page_object_model.pom_ForgotPassword import ForgotPassword


class Test1(EnvironmentSetup):

    def test1(self):
        pageUrl = "https://rahulshettyacademy.com/locatorspractice/"
        driver = self.driver
        self.driver.get(pageUrl)
        self.driver.implicitly_wait(20)
        time.sleep(2)

        main = PomLogin(driver)

        main.UserNameBar.send_keys('porag')
        time.sleep(2)
        main.PasswordBar.send_keys('123!@')
        time.sleep(2)
        main.SingInButton.click()
        time.sleep(2)

        main.ForgotYourPassword.click()
        self.driver.implicitly_wait(5)
        time.sleep(4)

        forgotPass = ForgotPassword(driver)

        forgotPass.NameBar.send_keys('porag')
        time.sleep(2)
        forgotPass.EmailBar.send_keys('test@gmail.com')
        time.sleep(2)
        forgotPass.PhoneNumberBar.send_keys('01257894163')
        time.sleep(3)
        forgotPass.ResetButton.click()
        time.sleep(2)
        # forgotPass.PickPass.get_Text()

        forgotPass.GoToLoginButton.click()
        self.driver.implicitly_wait(5)
        time.sleep(3)

        main.UserNameBar.send_keys("Porag")
        time.sleep(1)

        main.PasswordBar.send_keys("rahulshettyacademy")
        time.sleep(2)

        main.SingInButton.click()
        self.driver.implicitly_wait(5)
        time.sleep(5)
        print("LogIn Successfully")
