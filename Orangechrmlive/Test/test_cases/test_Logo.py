import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from Orangechrmlive.Src.base.environment_setup import EnvironmentSetup


@allure.severity(allure.severity_level.NORMAL)
class TestHRM(EnvironmentSetup):
    @allure.severity(allure.severity_level.MINOR)
    def test_Logo(self):
        pageUrl = "https://opensource-demo.orangehrmlive.com/"
        driver = self.driver
        self.driver.get(pageUrl)
        self.driver.implicitly_wait(20)
        time.sleep(2)

        status = self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[1]/img").is_displayed()
        if status == True:
            assert True
            print("Logo is here")
        else:
            assert False

    @allure.severity(allure.severity_level.NORMAL)
    def test_employeesList(self):
        pytest.skip("Skipping test...later I will implement...")
        pageUrl = "https://opensource-demo.orangehrmlive.com/"
        driver = self.driver
        self.driver.get(pageUrl)
        self.driver.implicitly_wait(20)
        time.sleep(2)

    @allure.severity(allure.severity_level.CRITICAL)
    def test_Login(self):
        pageUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver = self.driver
        self.driver.get(pageUrl)
        self.driver.implicitly_wait(20)
        time.sleep(2)

        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH,
                                 "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[3]/button[1]").click()
        time.sleep(4)
        act_title = driver.title

        if act_title == "OrangeHRM":
            self.driver.close()
            assert True

        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="testLogin", attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False
