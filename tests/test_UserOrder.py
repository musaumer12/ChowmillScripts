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


class TestOrderUSer(BaseClass):
    def test_UserOder(self, GetUser):
        log = self.GetLogger()
        signin = SignIn(self.driver)
        yourorder = YourOrders(self.driver)
        self.driver.implicitly_wait(5)
        signin.Get_Email().send_keys(GetUser["user"])
        signin.Get_Password().send_keys(GetUser["Pass"])
        signin.SignIn_Button().click()
        time.sleep(6)

        yourorder.Thai_item2().click()

        yourorder.AddtoOrder().click()
        log.info("adding dish to Order")
        time.sleep(4)
        log.info("extracting text form order Received pop up")
        msg = yourorder.Order_Recieved().text
        assert "You’re All Set!" in msg, "Order Failed for Company User"

    @pytest.fixture(params=SigninData.test_signin_data_user)
    def GetUser(self, request):
        return request.param
