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


class TestOrder(BaseClass):

    def test_AdminOrder(self, GetData):
        log = self.GetLogger()
        signin = SignIn(self.driver)
        yourorder = YourOrders(self.driver)
        self.driver.implicitly_wait(5)
        signin.Get_Email().send_keys(GetData["Email"])
        log.info("Adding Email")
        signin.Get_Password().send_keys(GetData["Password"])
        log.info("Adding Password")
        signin.SignIn_Button().click()
        log.info("Clicking on Sign in Button ")
        time.sleep(5)
        log.info("Clicking on Dish")
        yourorder.Thai_item().click()
        log.info("Selection option from options sets")
        #yourorder.Radio_button().click()
        yourorder.AddtoOrder().click()
        log.info("adding dish to Order")
        log.info("extracting text form order Received pop up")
        msg = yourorder.Order_Recieved().text
        assert "You’re All Set!" in msg, "Order Failed For Admin"


#class TestOrderUser(BaseClass):


    @pytest.fixture(params=SigninData.test_signin_data)
    def GetData(self, request):
        return request.param

