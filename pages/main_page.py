from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page

class MainPage(Page):

    def open_main_page(self):
        self.open_url('https://soft.reelly.io')


    SETTINGS_BUTTON_FIELD = (By.XPATH, "//span[text()='Settings']")

    def click(self, *locator):
        self.click(By.XPATH, "//span[text()='Settings']")
        sleep(10)