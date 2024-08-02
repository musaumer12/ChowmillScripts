from selenium.webdriver.common.by import By

class MarketPlace():

    new_delivery = (By.XPATH, "//button [@class='nav-link prim-link btn btn-sm btn-custom-primary new-delivery d-flex align-items-center ']")
    Address = (By.NAME, "selectedCompanyAddress")
    companyAddress = (By.XPATH, "//h6[text()='2762 Baton Rouge Dr, San Jose']")
    Addresses_locator = (By.XPATH, "//input[@class='mx-3']")
    AddressDone = (By.XPATH, "//button[text()='Done']")
# For all items //div/div/div/div/div/div/div/div/div/div/div/h6
    item = (By.XPATH, "//h6[text()='Pad See Ew']")
    flag = (By.NAME, "Idk")
    radio = (By.ID, "4729")
    add_to_order = (By.ID, "buybutton123")
    OrderRecieved = (By.XPATH, "//p[@class='text-center']")
    view = (By.XPATH, "//span[@class='fas fa-eye ml-2 fa-sm cursor-pointer']")
    okay = (By.XPATH, "//button[@class='ml-3 btn btn-primary buy-button buy-btn-wide']")

    def __init__(self, driver):
        self.driver = driver

    def NewDelivery(self):
        return self.driver.find_element(*MarketPlace.new_delivery)

    def address(self):
        return self.driver.find_element(*MarketPlace.Address)

    def get_addresses(self):  # Renamed from Addresses to get_addresses
        return self.driver.find_elements(*MarketPlace.Addresses_locator)

    def DeliveryAddress(self):
        return self.driver.find_element(*MarketPlace.companyAddress)

    def AddressConfirm(self):
        return self.driver.find_element(*MarketPlace.AddressDone)

    def GetItem(self):
        return self.driver.find_element(*MarketPlace.item)

    def SelectFlag(self):
        return self.driver.find_element(*MarketPlace.flag)

    def SelectRadioButton(self):
        return self.driver.find_element(*MarketPlace.radio)

    def AddtoOrder(self):
        return self.driver.find_element(*MarketPlace.add_to_order)

    def Confirmation(self):
        return self.driver.find_element(*MarketPlace.OrderRecieved)

    def ViewDetails(self):
        return self.driver.find_element(*MarketPlace.view)

    def OkayButton(self):
        return self.driver.find_element(*MarketPlace.okay)