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
        test_name = "Gender Selection"
        self.driver = setup
        TestTools.get_page_maximize_window(self.driver, UserRegistrationPage.url)
        registration_page = UserRegistrationPage(self.driver)
        genders = ["m", "f"]
        rando = random.randint(0, 1)
        registration_page.select_gender(genders[rando])
        if registration_page.verify_gender_selection(genders[rando]):
            TestTools.pass_test(self.driver, registration_page.page_name, test_name, genders[rando])
        else:
            TestTools.fail_test(self.driver, registration_page.page_name, test_name, True)

    def test_register_user_only_required_fields(self, setup):
        test_name = "Register User Required Fields Only"
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
            TestTools.pass_test(self.driver, registration_page.page_name, test_name)
        else:
            TestTools.fail_test(self.driver, registration_page.page_name, test_name, True)

    def test_email_already_registered(self, setup):
        test_name = "Email Already Registered"
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
            error_message = self.driver.find_element(By.XPATH, UserRegistrationPage.registration_error_xpath).text
            if error_message == "The specified email already exists":
                TestTools.pass_test(self.driver, registration_page.page_name, test_name)
            else:
                TestTools.fail_test(self.driver, registration_page.page_name, test_name, True, "Error text mismatch")
        else:
            TestTools.fail_test(self.driver, registration_page.page_name, test_name, True, "Missing erorr text")

    def test_first_name_requirement(self, setup):
        test_name = "First Name Required Error"
        self.driver = setup
        TestTools.get_page_maximize_window(self.driver, UserRegistrationPage.url)
        registration_page = UserRegistrationPage(self.driver)
        registration_page.click_register()
        time.sleep(2)
        if TestTools.check_for_element(self.driver, "ID", UserRegistrationPage.first_name_error_id):
            error_message = self.driver.find_element(By.ID, UserRegistrationPage.first_name_error_id).text
            if error_message == "First name is required.":
                TestTools.pass_test(self.driver, registration_page.page_name, test_name)
            else:
                TestTools.fail_test(self.driver, registration_page.page_name, test_name, True, "Error text mismatch")
        else:
            TestTools.fail_test(self.driver, registration_page.page_name, test_name, True, "Missing error text")

    def test_last_name_requirement(self, setup):
        test_name = "Last Name Required Error"
        self.driver = setup
        TestTools.get_page_maximize_window(self.driver, UserRegistrationPage.url)
        registration_page = UserRegistrationPage(self.driver)
        registration_page.click_register()
        time.sleep(2)
        if TestTools.check_for_element(self.driver, "ID", UserRegistrationPage.last_name_error_id):
            error_message = self.driver.find_element(By.ID, UserRegistrationPage.last_name_error_id).text
            if error_message == "Last name is required.":
                TestTools.pass_test(self.driver, registration_page.page_name, test_name)
            else:
                TestTools.fail_test(self.driver, registration_page.page_name, test_name, True, "Error text mismatch")
        else:
            TestTools.fail_test(self.driver, registration_page.page_name, test_name, True, "Missing error text")

    def test_email_requirement(self, setup):
        test_name = "Email Required Error"
        self.driver = setup
        TestTools.get_page_maximize_window(self.driver, UserRegistrationPage.url)
        registration_page = UserRegistrationPage(self.driver)
        registration_page.click_register()
        time.sleep(2)
        if TestTools.check_for_element(self.driver, "ID", UserRegistrationPage.email_error_id):
            error_message = self.driver.find_element(By.ID, UserRegistrationPage.email_error_id).text
            if error_message == "Email is required.":
                TestTools.pass_test(self.driver, registration_page.page_name, test_name)
            else:
                TestTools.fail_test(self.driver, registration_page.page_name, test_name, True, "Error text mismatch")
        else:
            TestTools.fail_test(self.driver, registration_page.page_name, test_name, True, "Missing error text")

    def test_password_requirement(self, setup):
        test_name = "Password Required Error"
        self.driver = setup
        TestTools.get_page_maximize_window(self.driver, UserRegistrationPage.url)
        registration_page = UserRegistrationPage(self.driver)
        registration_page.click_register()
        time.sleep(2)
        if TestTools.check_for_element(self.driver, "ID", UserRegistrationPage.confirm_password_error_id):
            error_message = self.driver.find_element(By.ID, UserRegistrationPage.confirm_password_error_id).text
            if error_message == "Password is required.":
                TestTools.pass_test(self.driver, registration_page.page_name, test_name)
            else:
                TestTools.fail_test(self.driver, registration_page.page_name, test_name, True, "Error text mismatch")
        else:
            TestTools.fail_test(self.driver, registration_page.page_name, test_name, True, "Missing error text")

    def test_password_length(self, setup):
        test_name = "Password Length"
        self.driver = setup
        TestTools.get_page_maximize_window(self.driver, UserRegistrationPage.url)
        registration_page = UserRegistrationPage(self.driver)
        registration_page.enter_password("abc")
        time.sleep(2)
        TestTools.press_key(self.driver, "tab")
        time.sleep(2)
        if TestTools.check_for_element(self.driver, "ID", UserRegistrationPage.password_error_id):
            error_message = self.driver.find_element(By.ID, UserRegistrationPage.password_error_id).text
            if error_message == UserRegistrationPage.password_requirement_text:
                TestTools.pass_test(self.driver, registration_page.page_name, test_name)
            else:
                TestTools.fail_test(self.driver, registration_page.page_name, test_name, True, "Error text mismatch")
        else:
            TestTools.fail_test(self.driver, registration_page.page_name, test_name, True, "Missing error text")

    def test_password_mismatch(self, setup):
        test_name = "Password Mismatch"
        self.driver = setup
        TestTools.get_page_maximize_window(self.driver, UserRegistrationPage.url)
        registration_page = UserRegistrationPage(self.driver)
        registration_page.enter_password(self.password)
        registration_page.enter_confirm_password(self.password[:-1])
        time.sleep(2)
        TestTools.press_key(self.driver, "tab")
        time.sleep(2)
        if TestTools.check_for_element(self.driver, "ID", UserRegistrationPage.confirm_password_error_id):
            error_message = self.driver.find_element(By.ID, UserRegistrationPage.confirm_password_error_id).text
            if error_message == "The password and confirmation password do not match.":
                TestTools.pass_test(self.driver, registration_page.page_name, test_name)
            else:
                TestTools.fail_test(self.driver, registration_page.page_name, test_name, True, "Error text mismatch")
        else:
            TestTools.fail_test(self.driver, registration_page.page_name, test_name, True, "Missing error text")
