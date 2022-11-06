from selenium.webdriver.common.by import By

class Register(object):
    def __init__(self, driver):
        self.driver = driver

        self.username = "Student25"
        self.password = "Student25Password!"
        self.rpassword = "Student25Password!"
        self.firstname = "Anna"
        self.lastname = "Yatsenko"
        self.email = "qwykeblu@gmail.com"
        self.phone = "0957467548"
        self.adr1 = "adr1"
        self.adr2 = "adr2"
        self.city = "Dnipro"
        self.state = "state"
        self.zip_code = "49128"
        self.country = "Ukraine"

        self.username_locator = (By.NAME, "username")
        self.password_locator = (By.NAME, "password")
        self.rpassword_locator = (By.NAME, "repeatedPassword")
        self.firstname_locator = (By.NAME, "account.firstName")
        self.lastname_locator = (By.NAME, "account.lastName")
        self.email_locator = (By.NAME, "account.email")
        self.phone_locator = (By.NAME, "account.phone")
        self.adr1_locator = (By.NAME, "account.address1")
        self.adr2_locator = (By.NAME, "account.address2")
        self.city_locator = (By.NAME, "account.city")
        self.state_locator = (By.NAME, "account.state")
        self.zip_code_locator = (By.NAME, "account.zip")
        self.country_locator = (By.NAME, "account.country")
        self.reg_btn_locator = (By.NAME, "newAccount")
        self.reg_btn_1_locator = (By.LINK_TEXT, "Register Now!")

        # 3classes chained - will use a CSS selector: self.login_button = ".fa.fa-2x.fa-sign-in"
        self.login_button = (By.NAME, "signon")

    def register(self):
        self.driver.find_element(*Register.username_locator).send_keys(self.username)
        self.driver.find_element(*Register.password_locator).send_keys(self.password)
        self.driver.find_element(*Register.rpassword_locator).send_keys(self.rpassword)
        self.driver.find_element(*Register.firstname_locator).send_keys(self.firstname)
        self.driver.find_element(*Register.lastname_locator).send_keys(self.lastname)
        self.driver.find_element(*Register.email_locator).send_keys(self.email)
        self.driver.find_element(*Register.adr1_locator).send_keys(self.adr1)
        self.driver.find_element(*Register.adr2_locator).send_keys(self.adr2)
        self.driver.find_element(*Register.city_locator).send_keys(self.city)
        self.driver.find_element(*Register.state_locator).send_keys(self.state)
        self.driver.find_element(*Register.zip_code_locator).send_keys(self.zip_code)
        self.driver.find_element(*Register.country_locator).send_keys(self.country)
        self.driver.find_element(*Register.reg_btn_locator).click()  # self.driver.find_element(By.name, self.login_button).click()