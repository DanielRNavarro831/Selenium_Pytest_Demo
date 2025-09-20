from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.read_properties import ReadConfig
from selenium.webdriver.support.ui import Select


class SearchPage:
    first_result_class = "product-title"
    page_name = "Search Results"

    def __init__(self, driver: webdriver):
        self.driver = driver

    def get_first_search_result(self):
        first_result = self.driver.find_element(By.CLASS_NAME, self.first_result_class)
        return first_result

