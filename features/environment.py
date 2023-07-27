import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options as ChromeOptions
from allure_commons.types import AttachmentType
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

from app.application import Application
from support.logger import logger


#########  Allure command ############################
# python3 -m behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/product_page_ui.feature
#######################################################


def browser_init(context, test_name):


# def browser_init(context):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """
    ####### GOOGLE CHROME ######################
    # service = Service()
    # options = webdriver.ChromeOptions()
    # context.driver = webdriver.Chrome(service=service, options=options)
    ############################################

    ######## HEADLESS MODE ########################
    # driver_path = ChromeDriverManager().install()
    # service = Service(executable_path=r'C/Users/priscillao/QA/Cureskin/chromedriver')
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--window-size=1920,1080')
    # context.driver = webdriver.Chrome(options=options,service=service)
    ###############################################

    ##################### FIREFOX #########################
    # driver_path = GeckoDriverManager().install()
    # service = FirefoxService(executable_path='/Users/priscillao/QA/Cureskin/geckodriver')
    # options = webdriver.FirefoxOptions()
    # context.driver = webdriver.Firefox(service=service,options=options)
    ########################################################

    ###################### BROWSERSTACK######################
    # options = ChromeOptions()
    # bs_user = 'bolanleoso_tj7eAn'
    # bs_key = 'sYVfdEQpAKsppEKyy5qK'
    #
    # # Setting the capabilities
    # caps = {
    #     "os": "OS X",
    #     "osVersion": "Ventura",
    #     "sessionName": test_name
    # }
    #
    # options.set_capability('bstack:options', caps)
    # options.set_capability('browserVersion', '95')
    # options.set_capability('browserName', 'Chrome')
    #
    # # connecting the test to Browserstack
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(
    #     command_executor=url,
    #     options=options)
    #################################################################


   ##################### MOBILE EMULATION ############################
    service = Service()
    options = webdriver.ChromeOptions()
    mobile_emulation = { "deviceName": "Nexus 5X" }
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    context.driver = webdriver.Chrome(service=service,options=options)
    context.driver.get('https://shop.cureskin.com/')

##################################################################################

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
        # context.driver.execute_script(
        #     'browserstack_executor: {"action": "setSessionStatus", "arguments": '
        #     '{"status":"failed", "reason": "Step failed"}}'

        # )

 ################## Attach a screenshot to Allure report in case the step fails: #############
        allure.attach(
            context.driver.get_screenshot_as_png(),
            name=f'{step.name}.png',
            attachment_type=AttachmentType.PNG
        )
  ##############################################################################################

def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()


