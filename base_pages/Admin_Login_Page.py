from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.read_properties import ReadConfig


class LoginAdminPage:
    email_field_id = "Email"
    password_field_id = "Password"
    login_button_xpath = "//button[@type='submit']"
    remember_me_id = "RememberMe"
    password_eye_closed_class = "password-eye"
    password_eye_open_xpath = "//span[@class='password-eye password-eye-open']"
    login_page_title = "nopCommerce demo store. Login"
    url = ReadConfig.get_admin_login_url()

    def __init__(self, driver: webdriver):
        self.driver = driver

    def enter_username(self, username: str):
        username_field = self.driver.find_element(By.ID, self.email_field_id)
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password: str):
        password_field = self.driver.find_element(By.ID, self.password_field_id)
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element(By.XPATH, self.login_button_xpath)
        login_button.click()

    def check_remember_me(self):
        remember_me = self.driver.find_element(By.ID, self.remember_me_id)
        remember_me.click()

    def reveal_password(self):
        password_eye = self.driver.find_element(By.CLASS_NAME, self.password_eye_closed_class)
        password_eye.click()

    def hide_password(self):
        password_eye = self.driver.find_element(By.XPATH, self.password_eye_open_xpath)
        password_eye.click()

    def get_password_text(self):
        password_field = self.driver.find_element(By.ID, self.password_field_id)
        password_text = password_field.get_attribute("value")
        return password_text

    def get_username_text(self):
        username_field = self.driver.find_element(By.ID, self.email_field_id)
        username_text = username_field.get_attribute("value")
        return username_text
