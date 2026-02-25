from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    #context.driver = webdriver.Chrome()
    # context.driver = webdriver.Firefox()
    #context.driver = webdriver.Safari()
    # context.driver.maximize_window()
    #
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    # driver_path = BrowserstackDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Browserstack(service=service)

    #
    # driver_path = FirefoxDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    #            # HEADLESS MODE
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # context.driver = webdriver.Chrome (options=options
    #
    # # options = webdriver.FirefoxOptions()
    # # options.add_argument('headless')
    #
    # )



# Browserstack
#
    bs_user = 'crystal_3bUM7P'
    bs_key = 'aynUBfdawUsZsjBaD35B'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    options = Options()
    bstack_options = {
        'os' : "Windows",
        "osVersion" : "11",
        'browserName' : 'Firefox',
        'sessionName' : scenario_name
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

# # Allure
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/product_search.feature

# allure serve test_results/


    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()

