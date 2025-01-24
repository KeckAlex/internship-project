from tkinter.font import names

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

from app.application import Application
from support.logger import logger


def browser_init(context, scenario_name):
    """
    :param scenario_name:
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    # Command to run tests with Allure & Behave:
    # behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/target_search.feature
    # allure serve test_results/

    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)
    # context.driver = webdriver.Safari()

    ### BROWSERS WITH DRIVERS: provide path to the driver file ###
    # service = Service(executable_path='/Users/svetlanalevinsohn/careerist/19-python-selenium-automation/geckodriver')
    # context.driver = webdriver.Firefox(service=service)

    ### SAFARI ###
    # context.driver = webdriver.Safari()

    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    #
    # bs_user = 'alexkeck_6yOGWg'
    # bs_key = 'BGfnJ8iUHtQS9PE3w7DA'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     "os" : "Windows",
    #     "osVersion" : "11",
    #     'browserName': 'chrome',
    #     'sessionName': scenario_name
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    # Other BS Config

    # bs_user = 'alexkeck_6yOGWg'
    # bs_key = 'BGfnJ8iUHtQS9PE3w7DA'
    #
    # url = f'http://hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     "os": "Windows",
    #     "osVersion": "11",
    #     "browserName": "Chrome",
    #     "browserVersion": "latest",
    #     'sessionName': scenario_name
    # }
    #
    # options.set_capability('bstack:options', bstack_options)
    # options.set_capability('browserstack.user', bs_user)
    # options.set_capability('browserstack.key', bs_key)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 15)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    logger.info(f'\nStarted scenario: {scenario.name}')
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    logger.info(f'Started step: {step}')
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'Step failed: {step}')
        print('\nStep failed: ', step)


def after_scenario(context, scenario):
    logger.info(f"Finished scenario: {scenario.name}")
    print('\nFinished scenario: ', scenario.name)
    context.driver.quit()




