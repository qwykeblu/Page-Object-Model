from selenium.webdriver.common.by import By


class Info(object):
    def __init__(self,driver):
        self.driver = driver

    def click_sign_in(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign').click()

    def click_sign_up(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign').click() #add like test
        self.driver.find_element(By.LINK_TEXT, 'Register Now!').click()