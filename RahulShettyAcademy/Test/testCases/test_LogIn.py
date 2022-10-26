import time

import allure
from selenium.webdriver.common.by import By

from RahulShettyAcademy.Src.base.environment_setup import EnvironmentSetup
from RahulShettyAcademy.Src.page_object_model.pom_logIn_page import PomLogin
from RahulShettyAcademy.screen_shots.screen_shots import SS

ss_path = "/login/"


@allure.severity(allure.severity_level.CRITICAL)
class TestLogIn(EnvironmentSetup):
    @allure.severity(allure.severity_level.CRITICAL)
    def test1(self):
        pageUrl = "https://rahulshettyacademy.com/locatorspractice/"
        driver = self.driver
        self.driver.get(pageUrl)
        self.driver.implicitly_wait(20)
        time.sleep(2)

        main = PomLogin(driver)

        if main.UserNameBar.is_enabled():
            print("UserName Bar is enabled")
            main.UserNameBar.send_keys('porag')
            time.sleep(2)
        else:
            print("UserName bar is not enable")

        if main.PasswordBar.is_enabled():
            print("Password bar is enable")
            main.PasswordBar.send_keys('rahulshettyacademy')
            time.sleep(2)
        else:
            print("Password bar is not enable")

        if main.SingInButton.is_enabled():
            print("SingIn Button is enable")
            main.SingInButton.click()
            self.driver.implicitly_wait(5)
            time.sleep(2)
        else:
            print("SignIn button is not enable")

            ss = SS(driver)
            file_name = ss_path + "Test-1_scrrenshot_" + time.asctime().replace(":", "_") + ".png"

            ss.driver.save_screenshot(file_name)
            ss.ScreenShot(file_name)

            status = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/h1/strong").is_displayed()
            if status == True:
                assert True
                print("Logo is here")
            else:
                assert False


