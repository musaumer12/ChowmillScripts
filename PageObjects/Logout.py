from selenium.webdriver.common.by import By

class Logout:
    profile = (By.XPATH, "from selenium.webdriver.common.by import By")
    button = (By.XPATH, "//a[@class='dropdown-item profiledropdownitem logout']")

    def __init__(self, driver):
        self.driver = driver

    def GetProfile(self):
        return self.driver.find_element(*Logout.profile)

    def LoggingOut(self):
        return self.driver.find_element(*Logout.button)