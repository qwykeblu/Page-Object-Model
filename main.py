from selenium import webdriver
from credentials import DRIVER_PATH, LINK
from pages.loginpage import *
from pages.infopage import *
from pages.registerpage import *

def setup():
    return webdriver.Edge(executable_path=DRIVER_PATH)


def logintest():
    driver = setup()

    driver.get(LINK)
    driver.maximize_window()

    welcome_page = Info(driver)
    welcome_page.click_sign_in()
    login_form = Login(driver)
    login_form.login()
    driver.quit()


def registertest():
    driver = setup()

    driver.get(LINK)
    driver.maximize_window()

    welcome_page = Info(driver)
    welcome_page.click_sign_up()
    login_form = Register(driver)
    login_form.register()
    driver.quit()


if __name__ == "__main__":
    choice = input("Type of test: (login-test, register-test, add-test, delete-test, logout-test) ")
    if choice=="login-test":
        logintest()
    elif choice=="register-test":
        registertest()

    else:
        print("BYE")



