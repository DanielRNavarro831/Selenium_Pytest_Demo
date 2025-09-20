import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from utilities.logger import Logger


class TestTools:
    logger = Logger.log_generator()

    @staticmethod
    def check_for_element(driver: webdriver, method: str, locator: str):
        method = method.lower()
        methods = {"class": By.CLASS_NAME,
                   "id": By.ID,
                   "xpath": By.XPATH,
                   "css selector": By.CSS_SELECTOR,
                   "link text": By.LINK_TEXT,
                   "partial link text": By.PARTIAL_LINK_TEXT,
                   "name": By.NAME,
                   "tag name": By.TAG_NAME}
        by = methods[method]
        try:
            driver.find_element(by, locator)
            return True
        except:
            print(f"Element not found using {method}: {locator}")
            return False

    @staticmethod
    def get_page_maximize_window(driver: webdriver, url: str):
        driver.get(url)
        driver.maximize_window()
        time.sleep(2)

    @staticmethod
    def press_key(driver: webdriver, key: str):
        key = key.lower()
        actions = ActionChains(driver)
        keys = {"tab": Keys.TAB, "enter": Keys.ENTER}
        actions = actions.send_keys(keys[key])
        actions.perform()

    @staticmethod
    def pass_test(driver: webdriver, page_name: str, test_name: str, passed_message=None):
        assert True
        passed_text = f" * {page_name}::{test_name}::Test Passed"
        if passed_message:
            passed_text += f" - {passed_message}"
        TestTools.logger.info(passed_text)
        driver.close()

    @staticmethod
    def fail_test(driver: webdriver, page_name: str, test_name: str, screenshot=False, error_message=None):
        failed_text = f" ! {page_name}::{test_name}::Test Failed"
        if error_message:
            failed_text += f" - {error_message}"
        TestTools.logger.info(failed_text)
        if screenshot:
            driver.save_screenshot(f".\\screenshots\\{page_name}_{test_name}.png")
        driver.close()
        assert False
