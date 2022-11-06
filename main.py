from selenium import webdriver
from selenium
from venv.pages.loginpage import *
from credentials import DRIVER_PATH, LINK

driver = webdriver.Edge(executable_path=DRIVER_PATH)
driver.get(LINK)
driver.maximize_window()


def setup():
    return webdriver.Chrome()


def logintest():
    driver = setup()

    driver.get("https://the-internet.herokuapp.com/login")

    login_form = Login(driver)
    login_form.login()
    driver.quit()

class LoginPage(page):
    def input_username(self, USERNAME):
        self.find_element(*Login.username).send_keys(USERNAME)

    def input_password(self, PASSWORD):
        self.find_element(*Login.password).send_keys(PASSWORD)


if __name__ == "__main__":
    user_choice = input("Would You like to  sign-in or register?")
    if user_choice == "sign-in":
        driver.find_element(By.LINK_TEXT, "Sign In").click()
    elif user_choice == "register":


