import time

# chrome driver
# -- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import pytest

from PageObjects.Logout import Logout
from PageObjects.YourOrders import YourOrders
from PageObjects.SignInPage import SignIn
from TestData.SigninData import SigninData
from utilities.BaseClass import BaseClass


driver = webdriver.Chrome()
driver.get("https://app-dev.chowmill.com/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.close()
driver.find_element(By.XPATH, )

list = ["Musa", "Umer", "9713"]
