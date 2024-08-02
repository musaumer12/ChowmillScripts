from selenium.webdriver.common.by import By



class YourOrders():
    date = (By.XPATH, "//p[@class='cursor-pointer text-nowrap delivery-date-time-heading mb-1']")
    mud_item1 = (By.XPATH, "//h6[text()='Spicy Tofu']")
    mud_item2 = (By.XPATH, "//h6[text()='Pineapple Fried Rice With Shrimp']")
    thai_item1 = (By.XPATH, "//h6[text()='Basil Chicken Fried Rice']")
    thai_item2 = (By.XPATH, "//h6[text()='Thai Shrimp Fried Rice']")
    radio = (By.ID, "4729")
    add_to_order = (By.ID, "buybutton")
    adding = (By.XPATH, "//button[@type='submit']")
    OrderRecieved = (By.XPATH, "//p[@class='text-center']")

    def __init__(self, driver):
        self.driver = driver

    def selectdate(self):
        return self.driver.find_element(*YourOrders.date)

    def SelectDish(self):
        return self.driver.find_element(*YourOrders.mud_item1)

    def SelectDishUser(self):
        return self.driver.find_element(*YourOrders.mud_item2)

    def Radio_button(self):
        return self.driver.find_element(*YourOrders.radio)

    def Thai_item(self):
        return self.driver.find_element(*YourOrders.thai_item1)

    def Thai_item2(self):
        return self.driver.find_element(*YourOrders.thai_item2)

    def AddtoOrder(self):
        return self.driver.find_element(*YourOrders.add_to_order)

    def Added(self):
        return self.driver.find_element(*YourOrders.adding)
    def Order_Recieved(self):
        return self.driver.find_element(*YourOrders.OrderRecieved)

