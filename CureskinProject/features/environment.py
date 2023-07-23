from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from app.application import Application
from support.logger import logger

def browser_init(context, test_name):


# def browser_init(context):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """
    ####### GOOGLE CHROME ######################
    # driver_path = ChromeDriverManager().install()
    # service = ChromeService(executable_path='/Users/priscillao/QA/Cureskin/chromedriver')
    # context.driver = webdriver.Chrome(service=service)
    ############################################

    ######## HEADLESS MODE ########################
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--window-size=1920,1080')
    # context.driver = webdriver.Chrome(options=options,service=service)
    ###############################################

    ##################### FIREFOX #########################
    # driver_path = GeckoDriverManager().install()
    # service = FirefoxService(driver_path)
    # context.driver = webdriver.Firefox(service=service)
    ########################################################

    ###################### BROWSERSTACK######################
    options = FirefoxOptions()
    bs_user = 'bolanleoso_tj7eAn'
    bs_key = 'sYVfdEQpAKsppEKyy5qK'

    # Setting the capabilities
    caps = {
        "os": "OS X",
        "osVersion": "Ventura",
        "sessionName": test_name
    }

    options.set_capability('bstack:options', caps)
    options.set_capability('browserVersion', '95')
    options.set_capability('browserName', 'Firefox')

    # connecting the test to Browserstack
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    context.driver = webdriver.Remote(
        command_executor=url,
        options=options)
    #################################################################

    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)

def before_step(context, step):
    print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        logger.error(f'Step failed: {step}')

        # Mark test case as FAILED on BrowserStack:
        # Documentation: https://www.browserstack.com/docs/automate/selenium/view-test-results/mark-tests-as-pass-fail
        context.driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": '
            '{"status":"failed", "reason": "Step failed"}}'
        )

def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()


