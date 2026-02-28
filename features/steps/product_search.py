from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_ICON = (By.CSS_SELECTOR,"[data-test='@web/CartIcon']")
HEADER_LINKS = (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")

SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')


@given('Open Google page')
def open_google(context):
    context.driver.get('https://www.google.com/')

# @given('Open Firefox page')
# def open_firefox(context):
#     context.driver.get('https://www.Firefox.com/')


@when('Search for {product}')
def search_product(context, product):
    context.app.header.search()

@then('Search results for {expected_product} are shown')
def verify_search_results(context, expected_product):
    context.app.search_results_page.verify_search_results()


@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(4)


@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(1)


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), \
        f'Expected query not in {context.driver.current_url.lower()}'

# Task 2 Internship

@given('Open the main page')
def open_google(context):
    # context.driver.get('https://soft.reelly.io')
    context.app.main_page.open_main_page()

# @given('Open Firefox page')
# def open_firefox(context):
#     sleep(5)
#     context.driver.get('https://soft.reelly.io')





@when('Log in to the page')
def click_login(context):
    sleep(5)
    context.app.login_page.login()
    # context.driver.find_element(By.CSS_SELECTOR,"[class='input w-input']").send_keys('crystalgjackson1987@gmail.com')
    # sleep(2)
    # context.driver.find_element(By.CSS_SELECTOR,"[data-name='Password']").send_keys('Bcbs2026!')
    # sleep(2)
    # context.driver.find_element(By.CSS_SELECTOR,"[class='login-button w-button']").click()


# @then('Click on "settings" at the left side menu')
# def click_settings(context):
#     sleep(15)
#     context.driver.find_element(By.XPATH, "//span[text()='Settings']").click()
#     # context.app.login_page.click()
#     sleep(15)

@then('Click on "market offers"')
def click_on_market_offers(context):
    sleep(15)
    context.driver.find_element(By.CSS_SELECTOR,'[class="font-medium text-xs whitespace-nowrap pt-8"]').click()
    sleep(25)

@then('Click on "menu" at the top left')
def click_menu(context):
    sleep(15)
    context.driver.find_elements(By.CSS_SELECTOR,'[class="new-market-menu-button _1 w-inline-block"]').click()
    # context.app.login_page.click()
    sleep(15)


@then('Click on the verification option')
def click_verification(context):
    sleep(15)
    context.driver.find_element(By.XPATH, "//a[contains(@href, 'verification') and contains(@class, 'page-setting')]").click()

@then('Verify the right page opens')
def verify_right_page(context):
    sleep(15)
    context.driver.find_elements(By.CSS_SELECTOR,"[class='setting-text']")

@then('Verify "upload image" and "Next step" buttons are available')
def verify_next_steps(context):
    # context.driver.find_element(By.CSS_SELECTOR,"[class='upload-button-2']")
    sleep(15)
    actual_text = context.driver.find_element(By.CSS_SELECTOR,"[class='next-step--']").text
    assert "Next step" in actual_text, f'expected Next step but got {actual_text}'
    sleep(15)
    actual_text = context.driver.find_element(By.CSS_SELECTOR,"[class='upload-button-2']").text
    assert "Upload image" in actual_text, f'expected Upload image but got {actual_text}'

