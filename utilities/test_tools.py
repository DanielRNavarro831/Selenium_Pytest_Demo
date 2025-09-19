import random
import time
import pytest
from selenium import webdriver
from base_pages.Home_Page import HomePage
from base_pages.User_Registration_Page import UserRegistrationPage
from utilities.doc_reader import DocReader
from utilities.logger import Logger
from selenium.webdriver.common.by import By


class TestTools:

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
            print("Element found!")
            return True
        except:
            print("Element not found :[")
            return False

    @staticmethod
    def get_page_maximize_window(driver: webdriver, url: str):
        driver.get(url)
        driver.maximize_window()
