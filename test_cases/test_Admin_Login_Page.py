import time
import pytest
from selenium import webdriver
from base_pages.Admin_Login_Page import AdminLoginPage
from base_pages.Admin_Dashboard import AdminDashboard
from selenium.webdriver.common.by import By
from utilities.read_properties import ReadConfig
from utilities.logger import Logger
from utilities.test_tools import TestTools


class TestLoginAdminPage:
    valid_username = ReadConfig.get_valid_admin_username()
    valid_password = ReadConfig.get_valid_admin_password()
    invalid_username = ReadConfig.get_invalid_admin_username()
    invalid_password = ReadConfig.get_invalid_admin_password()
    logger = Logger.log_generator()

    def test_page_title(self, setup):
        test_name = "Page Title"
        self.driver = setup
        TestTools.get_page_maximize_window(self.driver, AdminLoginPage.url)
        title = self.driver.title
        if title == AdminLoginPage.login_page_title:
            TestTools.pass_test(self.driver, AdminLoginPage.page_name, test_name)
        else:
            TestTools.fail_test(self.driver, AdminLoginPage.page_name, test_name)

    def test_invalid_username(self, setup):
        test_name = "Invalid Username"
        self.driver = setup
        TestTools.get_page_maximize_window(self.driver, AdminLoginPage.url)
        page = AdminLoginPage(self.driver)
        page.enter_username(self.invalid_username)
        page.enter_password(self.valid_password)
        page.click_login_button()
        time.sleep(3)
        if TestTools.check_for_element(self.driver, "xpath", "//li"):  # If error message exists...
            error_message = self.driver.find_element(By.XPATH, "//li").text
            if error_message == "No customer account found":
                TestTools.pass_test(self.driver, page.page_name, test_name)
            else:  # Wrong error message
                TestTools.fail_test(self.driver, page.page_name, test_name, True, "Error text mismatch")
        else:  # Error message not appearing
            TestTools.fail_test(self.driver, page.page_name, test_name, True, "Missing error test")

    def test_invalid_password(self, setup):
        test_name = "Invalid Password"
        self.driver = setup
        TestTools.get_page_maximize_window(self.driver, AdminLoginPage.url)
        page = AdminLoginPage(self.driver)
        page.enter_username(self.valid_username)
        page.enter_password(self.invalid_password)
        page.click_login_button()
        time.sleep(3)
        if TestTools.check_for_element(self.driver, "xpath", "//li"):  # If error message exists...
            error_message = self.driver.find_element(By.XPATH, "//li").text
            if error_message == "The credentials provided are incorrect":
                TestTools.pass_test(self.driver, page.page_name, test_name)
            else:  # Wrong error message
                TestTools.fail_test(self.driver, page.page_name, test_name, True, "Error text mismatch")
        else:  # Error message not appearing
            TestTools.fail_test(self.driver, page.page_name, test_name, True, "Missing error text")

    def test_valid_login(self, setup):
        test_name = "Valid Login"
        self.driver = setup
        TestTools.get_page_maximize_window(self.driver, AdminLoginPage.url)
        page = AdminLoginPage(self.driver)
        page.enter_username(self.valid_username)
        page.enter_password(self.valid_password)
        page.click_login_button()
        time.sleep(3)
        title = self.driver.title
        if title == AdminDashboard.dashboard_page_title:
            TestTools.pass_test(self.driver, page.page_name, test_name)
        else:
            TestTools.fail_test(self.driver, page.page_name, test_name, True)

    def test_reveal_password(self, setup):
        test_name = "Reveal Password"
        self.driver = setup
        TestTools.get_page_maximize_window(self.driver, AdminLoginPage.url)
        page = AdminLoginPage(self.driver)
        page.enter_password(self.valid_password)
        page.reveal_password()
        password_type = self.driver.find_element(By.ID, page.password_field_id).get_attribute("type")
        if password_type == "text":  # Field displays password as text
            TestTools.pass_test(self.driver, page.page_name, test_name)
        else:
            TestTools.fail_test(self.driver, page.page_name, test_name, True)

    def test_hide_password(self, setup):
        test_name = "Hide Password"
        self.driver = setup
        TestTools.get_page_maximize_window(self.driver, AdminLoginPage.url)
        page = AdminLoginPage(self.driver)
        page.enter_password(self.valid_password)
        time.sleep(2)
        page.reveal_password()
        time.sleep(2)
        page.hide_password()
        time.sleep(2)
        password_type = self.driver.find_element(By.ID, page.password_field_id).get_attribute("type")
        if password_type == "password":  # Field displays hidden password
            TestTools.pass_test(self.driver, page.page_name, test_name)
        else:
            TestTools.fail_test(self.driver, page.page_name, test_name, True)

    def test_remember_me(self, setup):
        test_name = "Remember Me"
        self.driver = setup
        TestTools.get_page_maximize_window(self.driver, AdminLoginPage.url)
        login_page = AdminLoginPage(self.driver)
        login_page.enter_username(self.valid_username)
        login_page.enter_password(self.valid_password)
        login_page.check_remember_me()
        login_page.click_login_button()
        time.sleep(3)
        dashboard_page = AdminDashboard(self.driver)
        dashboard_page.logout()
        time.sleep(3)
        username_text = login_page.get_username_text()
        if username_text == self.valid_username:
            TestTools.pass_test(self.driver, login_page.page_name, test_name)
        else:
            TestTools.fail_test(self.driver, login_page.page_name, test_name, True)
