import time

import allure
import pytest
from Orangechrmlive.Src.base.environment_setup import EnvironmentSetup


@allure.severity(allure.severity_level.NORMAL)
class TestEmployee(EnvironmentSetup):
    @allure.severity(allure.severity_level.NORMAL)
    def test_employeesList(self):
        pytest.skip("Skipping test...later I will implement...")
        pageUrl = "https://opensource-demo.orangehrmlive.com/"
        driver = self.driver
        self.driver.get(pageUrl)
        self.driver.implicitly_wait(20)
        time.sleep(2)
