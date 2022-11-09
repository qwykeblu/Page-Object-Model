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

        self.username_locator = ("username")
        self.password_locator = ("password")
        self.rpassword_locator = ("repeatedPassword")
        self.firstname_locator = ("account.firstName")
        self.lastname_locator = ("account.lastName")
        self.email_locator = ("account.email")
        self.phone_locator = ("account.phone")
        self.adr1_locator = ("account.address1")
        self.adr2_locator = ("account.address2")
        self.city_locator = ("account.city")
        self.state_locator = ("account.state")
        self.zip_code_locator = ("account.zip")
        self.country_locator = ("account.country")
        self.reg_btn_locator = ("newAccount")
        self.reg_btn_1_locator = ("Register Now!")

        # 3classes chained - will use a CSS selector: self.login_button = ".fa.fa-2x.fa-sign-in"
        self.login_button = (By.NAME, "signon")

    def register(self):
        self.driver.find_element(By.NAME, self.username_locator).send_keys(self.username)
        self.driver.find_element(By.NAME, self.password_locator).send_keys(self.password)
        self.driver.find_element(By.NAME, self.rpassword_locator).send_keys(self.rpassword)
        self.driver.find_element(By.NAME, self.firstname_locator).send_keys(self.firstname)
        self.driver.find_element(By.NAME, self.lastname_locator).send_keys(self.lastname)
        self.driver.find_element(By.NAME, self.email_locator).send_keys(self.email)
        self.driver.find_element(By.NAME, self.adr1_locator).send_keys(self.adr1)
        self.driver.find_element(By.NAME, self.adr2_locator).send_keys(self.adr2)
        self.driver.find_element(By.NAME, self.city_locator).send_keys(self.city)
        self.driver.find_element(By.NAME, self.state_locator).send_keys(self.state)
        self.driver.find_element(By.NAME, self.zip_code_locator).send_keys(self.zip_code)
        self.driver.find_element(By.NAME, self.country_locator).send_keys(self.country)
        self.driver.find_element(By.LINK_TEXT, self.reg_btn_locator).click()  # self.driver.find_element(By.name, self.login_button).click()