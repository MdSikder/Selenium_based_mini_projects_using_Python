from selenium import webdriver


class SS(object):

    def __init__(self, driver):
        self.driver = driver

    def ScreenShot(self, path):
        directory = "C:/Users/User/PycharmProjects/Selenium_based_mini_projects_using_python/RahulShettyAcademy/screen_shots"
        self.driver.get_screenshot_as_file(directory + path)


"""file_name = path + "scrrenshot_" + time.asctime().replace(":", "_") + ".png"
    d.save_screenshot(file_name) """