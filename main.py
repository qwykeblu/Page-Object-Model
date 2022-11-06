from selenium import webdriver
from credentials import DRIVER_PATH, LINK
from pages.loginpage import *





def setup():
    return webdriver.Edge(executable_path=DRIVER_PATH)


def logintest():
    driver = setup()

    driver.get(LINK)
    driver.maximize_window()

    login_form = Login(driver)
    login_form.login()
    driver.quit()

# class LoginPage(page):
#     def input_username(self, USERNAME):
#         self.find_element(*Login.username).send_keys(USERNAME)
#
#     def input_password(self, PASSWORD):
#         self.find_element(*Login.password).send_keys(PASSWORD)


if __name__ == "__main__":
    logintest()


