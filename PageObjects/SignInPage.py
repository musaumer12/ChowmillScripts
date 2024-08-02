from selenium.webdriver.common.by import By


class SignIn:

    email = (By.NAME, "email")
    password = (By.NAME, "password")
    button = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def Get_Email(self):

        return self.driver.find_element(*SignIn.email)

    def Get_Password(self):
        return self.driver.find_element(*SignIn.password)

    def SignIn_Button(self):
        return self.driver.find_element(*SignIn.button)


