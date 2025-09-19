import random
import time
import pytest
from selenium import webdriver
from base_pages.Home_Page import HomePage
from base_pages.User_Registration_Page import UserRegistrationPage
from utilities.doc_reader import DocReader
from utilities.logger import Logger
from utilities.test_tools import TestTools
from selenium.webdriver.common.by import By


class TestRegistrationPage:
    logger = Logger.log_generator()
    first_name = "Testy"
    last_name = "McTesterson"
    password = "Testing"
    email = DocReader.get_cell_value_string("Registration", "Registration Email")
    used_email = DocReader.get_cell_value_string("Registration", "Used Email")

    @staticmethod
    def update_email():
        DocReader.update_registration_email_doc()
        TestRegistrationPage.email = DocReader.get_cell_value_string("Registration", "Registration Email")

    def test_gender_selection(self, setup):
        self.driver = setup
        TestTools.get_page_maximize_window(self.driver, UserRegistrationPage.url)
        registration_page = UserRegistrationPage(self.driver)
        genders = ["m", "f"]
        rando = random.randint(0, 1)
        registration_page.select_gender(genders[rando])
        if registration_page.verify_gender_selection(genders[rando]):
            assert True
            self.logger.info(f" * Registration Page::Gender Selection::{genders[rando]}::Test Passed")
            self.driver.close()
        else:
            self.logger.info(f" * Registration Page::Gender Selection::{genders[rando]}::Test Failed - radio button not clicked")
            self.driver.close()
            assert False

    def test_register_user_only_required_fields(self, setup):
        self.driver = setup
        TestTools.get_page_maximize_window(self.driver, UserRegistrationPage.url)
        registration_page = UserRegistrationPage(self.driver)
        registration_page.enter_first_name(self.first_name)
        registration_page.enter_last_name(self.last_name)
        TestRegistrationPage.update_email()
        time.sleep(3)
        registration_page.enter_email(self.email)
        registration_page.check_newsletter_box()
        registration_page.enter_password(self.password)
        registration_page.enter_confirm_password(self.password)
        registration_page.click_register()
        time.sleep(3)
        if TestTools.check_for_element(self.driver, "Class", registration_page.registration_confirmation_class):
            assert True
            self.logger.info(f" * Registration Page::Register User Required Fields Only::Email Used {self.email}::Test Passed")
            self.driver.close()
        else:
            self.logger.info(f" ! Registration Page::Register User Required Fields Only::Email Used {self.email}::Test Failed - No confirmation text")
            self.driver.close()
            assert False

    def test_email_already_exists(self, setup):
        self.driver = setup
        TestTools.get_page_maximize_window(self.driver, UserRegistrationPage.url)
        registration_page = UserRegistrationPage(self.driver)
        registration_page.enter_first_name(self.first_name)
        registration_page.enter_last_name(self.last_name)
        registration_page.enter_email(self.used_email)
        registration_page.enter_password(self.password)
        registration_page.enter_confirm_password(self.password)
        registration_page.click_register()
        time.sleep(3)
        if TestTools.check_for_element(self.driver, "xpath", UserRegistrationPage.registration_error_xpath):
            assert True
            self.logger.info(" * Registration Page::Email Already Registered::Test Passed")
            self.driver.close()
        else:
            self.logger.info(" ! Registration Page::Email Already Registered::Test Failed - Error text missing")
            self.driver.close()
            assert False
