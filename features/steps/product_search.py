from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')


@given('Open Google page')
def open_google(context):
    context.driver.get('https://www.google.com/')


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

# Test 1 Internship

@given('Open the main page')
def open_google(context):
    context.driver.get('https://soft.reelly.io')

@when('Log in to the page')
def click_login(context):
    context.driver.get('https://soft.reelly.io/sign-in')
    sleep(20)
    context.driver.find_element(By.CSS_SELECTOR,"[class='form-header']").click()


@then('Click on "settings" at the left side menu')
def click_settings(context):
    context.driver.find_element(By.CSS_SELECTOR,"[class='menu-button-block w-inline-block w--current']").click()
    sleep(20)

@then('Click on the verification option')
def click_verification(context):
    context.driver.find_element(By.CSS_SELECTOR,"[class='setting-text']").click()
    sleep(20)

@then('Verify the right page opens')
def verify_right_page(context):
    context.driver.find_element(By.CSS_SELECTOR,"[step-1-block']").click()
    sleep(20)

@then('Verify "upload image" and "Next step" buttons are available')
def verify_next_step(context):
    actual_text:context.driver.find_element(By.CSS_SELECTOR,"[class='upload-button-2']").text
    sleep(20)
    actual_text:context.driver.find_element(By.CSS_SELECTOR,"[class='button-verify margin-top-8 w-inline-block']").text
    assert'verify "upload image" and "Next step" buttons are available' in 'actual_text',f'expected verify "upload image" and "Next step" buttons are available''text not in {actual_text}'
    sleep(20)
