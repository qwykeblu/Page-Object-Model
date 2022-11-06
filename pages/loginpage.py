from selenium.webdriver.common.by import By

class Login(object):
    def __init__(self, driver):
        self.driver = driver

        self.username = "Student25"
        self.password = "Student25Password!"

        self.username_locator = (By.NAME, "username")
        self.password_locator = (By.NAME, "password")

        # 3classes chained - will use a CSS selector: self.login_button = ".fa.fa-2x.fa-sign-in"
        self.login_button = (By.NAME, "signon")

    def login(self):
        self.driver.find_element(*Login.username_locator).send_keys(self.username)
        self.driver.find_element(*Login.password_locator).send_keys(self.password)
        self.driver.find_element(*Login.login_button).click()  # self.driver.find_element(By.name, self.login_button).click()