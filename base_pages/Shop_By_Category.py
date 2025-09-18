import time
import pytest
from selenium import webdriver
from base_pages.Home_Page import HomePage
from base_pages.Search_Page import SearchPage
from utilities.logger import Logger
from selenium.webdriver.common.by import By


class ShopByCategory:
    category_header_class = "page-title"

    def __init__(self, driver: webdriver):
        self.driver = driver

    def get_category_header(self):
        header = self.driver.find_element(By.CLASS_NAME, self.category_header_class)
        return header.text

