import time

# chrome driver
# -- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import pytest

from PageObjects.Logout import Logout
from PageObjects.MarketPlace import MarketPlace
from PageObjects.YourOrders import YourOrders
from PageObjects.SignInPage import SignIn
from TestData.SigninData import SigninData
from utilities.BaseClass import BaseClass


class TestNewDelivery(BaseClass):

    def test_AdminNewDelivery(self, GetData):
        log = self.GetLogger()
        signin = SignIn(self.driver)
        marketplace = MarketPlace(self.driver)
        self.driver.implicitly_wait(5)
        signin.Get_Email().send_keys(GetData["Email"])
        log.info("Adding Email")
        signin.Get_Password().send_keys(GetData["Password"])
        log.info("Adding Password")
        signin.SignIn_Button().click()
        log.info("Clicking on Sign in Button ")
        time.sleep(5)

        marketplace.NewDelivery().click()
        marketplace.address().click()
        time.sleep(5)
        add = marketplace.get_addresses()
        for address in add:
            if address.get_attribute("value") == "1900":
                address.click()
            else:
                assert "Address do not exist"
        marketplace.AddressConfirm().click()
        marketplace.GetItem().click()
        marketplace.GetItem().click()
        marketplace.SelectFlag().click()
        marketplace.SelectRadioButton().click()
        marketplace.AddtoOrder().click()
        success = marketplace.Confirmation().text
        assert "You’re All Set!" in success, "Meeting is not created"
        marketplace.OkayButton().click()
        #marketplace.ViewDetails().click()

    @pytest.fixture(params= SigninData.test_signin_data)
    def GetData(self, request):
        return request.param
