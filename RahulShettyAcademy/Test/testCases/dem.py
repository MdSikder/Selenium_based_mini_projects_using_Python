import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from RahulShettyAcademy.Src.locators.locators import Locator
from RahulShettyAcademy.Src.base.environment_setup import EnvironmentSetup
from RahulShettyAcademy.Src.page_object_model.pom_logIn_page import PomLogin
from RahulShettyAcademy.Src.page_object_model.pom_ForgotPassword import ForgotPassword


class Test1(EnvironmentSetup):

    def test1(self):
        pageUrl = "https://rahulshettyacademy.com/locatorspractice/"
        driver = self.driver
        self.driver.get(pageUrl)
        self.driver.implicitly_wait(20)
        time.sleep(2)

        main = PomLogin(driver)

        titleOfWebPage = driver.title

        self.assertTrue(titleOfWebPage == "Sign in")
