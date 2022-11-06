from selenium.webdriver.common.by import By

class Info():
    def __init__(self,driver):
        self.driver = driver

        self.sign_up_link = (By.XPATH,"//*[@id='Content']/ul/li[1]/a")
        self.sign_in_link = (By.XPATH, "//*[@id='Content']/ul/li[2]/a")

        def click_sign_in(self):
            self.driver.find_element(*Info.sign_in_link).click()

        def click_sign_up(self):
            self.driver.find_element(*Info.sign_up_link).click()