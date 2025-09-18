import time
import pytest
from selenium import webdriver
from base_pages.Home_Page import HomePage
from base_pages.Search_Page import SearchPage
from base_pages.Shop_By_Category import ShopByCategory
from utilities.logger import Logger
from selenium.webdriver.common.by import By


class TestHomePage:
    logger = Logger.log_generator()

    def get_page_maximize_window(self):
        self.driver.get(HomePage.url)
        self.driver.maximize_window()

    def test_register_user(self, setup):
        self.driver = setup
        self.get_page_maximize_window()
        home_page = HomePage(self.driver)
        home_page.click_register()

    def test_search_for_items(self, setup):
        self.driver = setup
        self.get_page_maximize_window()
        home_page = HomePage(self.driver)
        time.sleep(3)
        home_page.enter_searchbox("phone")
        search_page = SearchPage(self.driver)
        results_text = search_page.get_first_search_result().text
        results_text = results_text.lower()
        if "phone" in results_text:
            assert True
            self.logger.info(" * Home Page::Search For Items::Test Passed")
            self.driver.close()
        else:
            self.logger.info(" * Home Page::Search For Items::Test Failed")
            self.driver.close()
            assert False

    def test_change_currency_to_euro(self, setup):
        self.driver = setup
        self.get_page_maximize_window()
        home_page = HomePage(self.driver)
        time.sleep(1)
        home_page.click_currency_dropdown("Euro")
        time.sleep(3)
        currency = home_page.check_currency()
        if currency == "Euro":
            assert True
            self.logger.info(" * Home Page::Change Currency to Euro::Test Passed")
            self.driver.close()
        else:
            self.logger.info(" * Home Page::Change Currency to Euro::Test Failed::$ symbol detected")
            self.driver.close()
            assert False

    def test_change_currency_to_dollar(self, setup):
        self.driver = setup
        self.get_page_maximize_window()
        home_page = HomePage(self.driver)
        time.sleep(1)
        home_page.click_currency_dropdown("US Dollar")
        time.sleep(3)
        currency = home_page.check_currency()
        if currency == "US Dollar":
            assert True
            self.logger.info(" * Home Page::Change Currency to Dollar::Test Passed")
            self.driver.close()
        else:
            self.logger.info(" * Home Page::Change Currency to Dollar::Test Failed::Euro symbol detected")
            self.driver.close()
            assert False

    def test_computers_desktops(self, setup):
        self.driver = setup
        self.get_page_maximize_window()
        home_page = HomePage(self.driver)
        time.sleep(1)
        home_page.click_computers("Desktops")
        time.sleep(3)
        shop_page = ShopByCategory(self.driver)
        category_header = shop_page.get_category_header()
        if category_header == "Desktops":
            assert True
            self.logger.info(" * Home Page::Computers Desktops Submenu::Test Passed")
            self.driver.close()
        else:
            self.logger.info(" ! Home Page::Computers Desktops Submenu::Test Failed")
            self.driver.close()
            assert False

    def test_computers_notebooks(self, setup):
        self.driver = setup
        self.get_page_maximize_window()
        home_page = HomePage(self.driver)
        time.sleep(1)
        home_page.click_computers("Notebooks")
        time.sleep(3)
        shop_page = ShopByCategory(self.driver)
        category_header = shop_page.get_category_header()
        if category_header == "Notebooks":
            assert True
            self.logger.info(" * Home Page::Computers Notebooks Submenu::Test Passed")
            self.driver.close()
        else:
            self.logger.info(" ! Home Page::Computers Notebooks Submenu::Test Failed")
            self.driver.close()
            assert False

    def test_computers_software(self, setup):
        self.driver = setup
        self.get_page_maximize_window()
        home_page = HomePage(self.driver)
        time.sleep(1)
        home_page.click_computers("Software")
        time.sleep(3)
        shop_page = ShopByCategory(self.driver)
        category_header = shop_page.get_category_header()
        if category_header == "Software":
            assert True
            self.logger.info(" * Home Page::Computers Software Submenu::Test Passed")
            self.driver.close()
        else:
            self.logger.info(" ! Home Page::Computers Software Submenu::Test Failed")
            self.driver.close()
            assert False
