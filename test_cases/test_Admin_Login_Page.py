import time
import pytest
from selenium import webdriver
from base_pages.Admin_Login_Page import LoginAdminPage
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
        self.driver = setup
        TestTools.get_page_maximize_window(self.driver, LoginAdminPage.url)
        title = self.driver.title
        if title == LoginAdminPage.login_page_title:
            assert True
            self.logger.info(" * Admin Login Page::Page Title::Test Passed")
            self.driver.close()
        else:
            self.logger.info(" ! Admin Login Page::Page Title::Test Failed::Page title mismatch - Taking screenshot")
            self.driver.save_screenshot(".\\screenshots\\page_title.png")
            self.driver.close()
            assert False

    def test_invalid_username(self, setup):
        self.driver = setup
        TestTools.get_page_maximize_window(self.driver, LoginAdminPage.url)
        page = LoginAdminPage(self.driver)
        page.enter_username(self.invalid_username)
        page.enter_password(self.valid_password)
        page.click_login_button()
        time.sleep(3)
        if TestTools.check_for_element(self.driver, "xpath", "//li"):  # If error message exists...
            error_message = self.driver.find_element(By.XPATH, "//li").text
            if error_message == "No customer account found":
                assert True
                self.logger.info(" * Admin Login Page::Invalid Username::Test Passed")
                self.driver.close()
            else:  # Wrong error message
                self.logger.info(" ! Admin Login Page::Invalid Username::Test Failed::Error text mismatch - Taking screenshot")
                self.driver.save_screenshot(".\\screenshots\\invalid_username_error.png")
                self.driver.close()
                assert False
        else:  # Error message not appearing
            self.logger.info(" ! Admin Login Page::Invalid Username::Test Failed::Error message not found - Taking screenshot")
            self.driver.save_screenshot(".\\screenshots\\invalid_username_error.png")
            self.driver.close()
            assert False

    def test_invalid_password(self, setup):
        self.driver = setup
        TestTools.get_page_maximize_window(self.driver, LoginAdminPage.url)
        page = LoginAdminPage(self.driver)
        page.enter_username(self.valid_username)
        page.enter_password(self.invalid_password)
        page.click_login_button()
        time.sleep(3)
        if TestTools.check_for_element(self.driver, "xpath", "//li"):  # If error message exists...
            error_message = self.driver.find_element(By.XPATH, "//li").text
            if error_message == "The credentials provided are incorrect":
                assert True
                self.logger.info(" * Admin Login Page::Invalid Password::Test Passed")
                self.driver.close()
            else:  # Wrong error message
                self.logger.info(" ! Admin Login Page::Invalid Password::Test Failed::Error text mismatch - Taking screenshot")
                self.driver.save_screenshot(".\\screenshots\\invalid_password_error.png")
                self.driver.close()
                assert False
        else:  # Error message not appearing
            self.logger.info(" ! Admin Login Page::Invalid Password::Test Failed::Error message not found - Taking screenshot")
            self.driver.save_screenshot(".\\screenshots\\invalid_password_error.png")
            self.driver.close()
            assert False

    def test_valid_login(self, setup):
        self.driver = setup
        TestTools.get_page_maximize_window(self.driver, LoginAdminPage.url)
        page = LoginAdminPage(self.driver)
        page.enter_username(self.valid_username)
        page.enter_password(self.valid_password)
        page.click_login_button()
        time.sleep(3)
        title = self.driver.title
        if title == AdminDashboard.dashboard_page_title:
            assert True
            self.logger.info(" * Admin Login Page::Valid Login::Test Passed")
            self.driver.close()
        else:
            self.logger.info(" ! Admin Login Page::Valid Login::Test Failed::Page title mismatch - Taking screenshot")
            self.driver.save_screenshot(".\\screenshots\\valid_login.png")
            self.driver.close()
            assert False

    def test_reveal_password(self, setup):
        self.driver = setup
        TestTools.get_page_maximize_window(self.driver, LoginAdminPage.url)
        page = LoginAdminPage(self.driver)
        page.enter_password(self.valid_password)
        page.reveal_password()
        password_type = self.driver.find_element(By.ID, page.password_field_id).get_attribute("type")
        if password_type == "text":  # Field displays password as text
            assert True
            self.logger.info(" * Admin Login Page::Reveal Password::Test Passed")
            self.driver.close()
        else:
            self.logger.info(" ! Admin Login Page::Reveal Password::Test Failed::Password not revealed - Taking screenshot")
            self.driver.save_screenshot(".\\screenshots\\reveal_password.png")
            self.driver.close()
            assert False

    def test_hide_password(self, setup):
        self.driver = setup
        TestTools.get_page_maximize_window(self.driver, LoginAdminPage.url)
        page = LoginAdminPage(self.driver)
        page.enter_password(self.valid_password)
        time.sleep(2)
        page.reveal_password()
        time.sleep(2)
        page.hide_password()
        time.sleep(2)
        password_type = self.driver.find_element(By.ID, page.password_field_id).get_attribute("type")
        if password_type == "password":  # Field displays hidden password
            assert True
            self.logger.info(" * Admin Login Page::Hide Password::Test Passed")
            self.driver.close()
        else:
            self.logger.info(" ! Admin Login Page::Hide Password::Test Failed::Password not hidden - Taking screenshot")
            self.driver.save_screenshot(".\\screenshots\\hide_password.png")
            self.driver.close()
            assert False

    def test_remember_me(self, setup):
        self.driver = setup
        TestTools.get_page_maximize_window(self.driver, LoginAdminPage.url)
        login_page = LoginAdminPage(self.driver)
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
            assert True
            self.logger.info(" * Admin Login Page::Remember Me::Test Passed")
            self.driver.close()
        else:
            self.logger.info(" ! Admin Login Page::Remember Me::Test Failed::Username not in username field - Taking screenshot")
            self.driver.save_screenshot(".\\screenshots\\remember_me_logout.png")
            self.driver.close()
            assert False
