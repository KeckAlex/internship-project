from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from support.logger import logger


class Page:
    def __init__(self, driver):  # in order to call this function: page = Page(selenium_driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=15)

    def open_url(self, url):
        logger.info(f"Opening url: {url}")
        self.driver.get(url)

    def find_element(self, *locator):
        logger.info(f"Finding element: {locator}")
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        logger.info(f"Finding elements: {locator}")
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        logger.info(f"Clicking element: {locator}")
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        logger.info(f"Inputting text: {text} for element: {locator}")
        self.driver.find_element(*locator).send_keys(text)

    def hover_element(self, *locator):
        logger.info(f"Hovering element: {locator}")
        element = self.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()

    def get_current_window(self):
        window = self.driver.current_window_handle
        print('Current window:', window)
        return window

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        windows = self.driver.window_handles
        print(f'All windows {windows}')
        self.driver.switch_to.window(windows[1])
        print(f'Switched to window => {windows[1]}')

    def switch_to_window_by_id(self, window_id):
        self.driver.switch_to.window(window_id)
        print(f'Switched to window => {window_id}')

    def close(self):
        logger.info(f"Closing {self.driver}")
        self.driver.close()

    def wait_to_be_clickable(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by locator {locator} not clickable'
        )

    def wait_and_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by locator {locator} not clickable'
        ).click()

    def wait_for_element_appear(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by locator {locator} did not appear'
        ).click()

    def wait_for_element_disappear(self, *locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element by locator {locator} shown, but should not appear'
        ).click()

    def verify_text(self, expected_text, *locator):
        logger.info(f"Verifying text: {expected_text}")
        actual_text = self.find_element(*locator).text
        assert actual_text == expected_text, f'Expected {expected_text} did not match actual {actual_text}'

    def verify_partial_text(self, expected_partial_text, *locator):
        logger.info(f"Verifying partial text: {expected_partial_text}")
        actual_text = self.driver.find_element(*locator).text
        assert expected_partial_text in actual_text, f'Expected {expected_partial_text} not in actual {actual_text}'

    def verify_url(self, expected_url):
        logger.info(f"Verifying url: {expected_url}")
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f'Expected {expected_url} did not match actual {actual_url}'

    def verify_partial_url(self, expected_partial_url):
        logger.info(f"Verifying partial url: {expected_partial_url}")
        actual_url = self.driver.current_url
        assert expected_partial_url in actual_url, f'Expected {expected_partial_url} not in actual {actual_url}'
