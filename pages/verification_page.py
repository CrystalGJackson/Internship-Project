from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page

class VerificationPage(Page):


    def click(self, *locator):
        self.click(By.XPATH, "//a[contains(@href, 'verification') and contains(@class, 'page-setting')]")
        sleep(10)


    def find_elements(self, *locator):
        self.click(By.CSS_SELECTOR,"[class='setting-text']")
        sleep(10)

    def find_element(self, *locator):
        self.find_element(By.CSS_SELECTOR,"[class='next-step--']")
        sleep(10)
        self.find_element(By.CSS_SELECTOR,"[class='upload-button-2']")
        sleep(10)