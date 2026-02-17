from features.steps.product_search import click_login
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.login_page import LoginPage
from pages.verification_page import VerificationPage

class Application:

    def __init__(self, driver):

        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.login_page = LoginPage(driver)

    # app = Application()
    # app.main_page....
    # app.header.input_text()
    # app.header.search()
