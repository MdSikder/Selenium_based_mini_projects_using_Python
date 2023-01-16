import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from RahulShettyAcademy.Src.locators.locators import Locator
from RahulShettyAcademy.Src.base.environment_setup import EnvironmentSetup
from RahulShettyAcademy.Src.page_object_model.pom_logIn_page import PomLogin
from RahulShettyAcademy.Src.page_object_model.pom_ForgotPassword import ForgotPassword


@allure.severity(allure.severity_level.NORMAL)
class TestForgotPass(EnvironmentSetup):
    @allure.severity(allure.severity_level.NORMAL)
    def test_forgot_pass(self):
        pageUrl = "https://rahulshettyacademy.com/locatorspractice/"
        driver = self.driver
        self.driver.get(pageUrl)
        self.driver.implicitly_wait(20)
        time.sleep(2)

        username = driver.find_element(By.ID, Locator.UserNameBar)
        username.send_keys('porag')
        time.sleep(2)

        password = driver.find_element(By.NAME, Locator.PasswordBar)
        password.send_keys('wrong_password')
        time.sleep(2)

        signinButton = driver.find_element(By.CLASS_NAME, Locator.signinButton)
        signinButton.click()
        time.sleep(5)

        forgot = driver.find_element(By.LINK_TEXT, Locator.ForgotYourPassword)
        forgot.click()
        time.sleep(1)

        name = driver.find_element(By.XPATH, Locator.NameBar)
        name.send_keys('porag')
        time.sleep(1)

        email = driver.find_element(By.XPATH, Locator.EmailBar)
        email.send_keys('porag@gmail.com')
        time.sleep(1)

        PhoneNumber = driver.find_element(By.CSS_SELECTOR, Locator.PhoneNumberBar)
        PhoneNumber.send_keys('01677001457')
        time.sleep(1)

        reset = driver.find_element(By.CSS_SELECTOR, Locator.ResetButton)
        reset.click()
        time.sleep(3)

        goToLogin = driver.find_element(By.CSS_SELECTOR, Locator.GoToLoginButton)
        goToLogin.click()
        time.sleep(3)

        username = driver.find_element(By.ID, Locator.UserNameBar)
        username.send_keys('porag')
        time.sleep(2)

        password = driver.find_element(By.NAME, Locator.PasswordBar)
        password.send_keys('rahulshettyacademy')
        time.sleep(2)

        signinButton = driver.find_element(By.CLASS_NAME, Locator.signinButton)
        signinButton.click()
        time.sleep(5)

        status = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/h1/strong").is_displayed()
        if status == True:
            assert True
            print("Logo is here")
        else:
            assert False

