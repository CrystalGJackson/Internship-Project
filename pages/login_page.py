from selenium.webdriver.common.by import By

from pages.base_page import Page

from time import sleep

class LoginPage(Page):

    EMAIL_FIELD = By.CSS_SELECTOR,"[class='input w-input']"
    PASSWORD_FIELD = By.CSS_SELECTOR,"[data-name='Password']"
    LOGIN_BUTTON_FIELD = By.CSS_SELECTOR, "[class='login-button w-button']"

    def __init__(self, driver):
        super().__init__(driver)
        self.By = None

    def login(self):
        self.input_text('crystalgjackson1987@gmail.com', *self.EMAIL_FIELD)
        sleep(5)
        self.input_text('Bcbs2026!', *self.PASSWORD_FIELD)
        self.click(By.CSS_SELECTOR, "[class='login-button w-button']")
        sleep(5)
        # self.click(By.XPATH, "//span[text()='Settings']")
        # sleep(5)

        # self.click(self, 'crystalgjackson1987@gmail.com', (*By.CSS_SELECTOR,"[class='input w-input']"

    # (By.CSS_SELECTOR,"[class='input w-input']")
    #
    # (By.CSS_SELECTOR, "[data-name='Password']")
    #
    # (By.CSS_SELECTOR, "[class='login-button w-button']")