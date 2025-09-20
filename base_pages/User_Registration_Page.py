from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.read_properties import ReadConfig


class UserRegistrationPage:
    gender_male_selection_id = "gender-male"
    gender_female_seelction_id = "gender-female"
    first_name_field_id = "FirstName"
    last_name_field_id = "LastName"
    email_field_id = "Email"
    company_field_id = "Company"
    newsletter_id = "Newsletter"
    password_id = "Password"
    confirm_password_id = "ConfirmPassword"
    register_button_id = "register-button"
    registration_confirmation_class = "result"
    registration_error_xpath = '//div[@class="message-error validation-summary-errors"]'
    first_name_error_id = "FirstName-error"
    last_name_error_id = "LastName-error"
    email_error_id = "Email-error"
    confirm_password_error_id = "ConfirmPassword-error"
    password_error_id = "Password-error"
    page_title = "nopCommerce demo store. Register"
    password_requirement_text = "Password must meet the following rules: must have at least 6 characters and not greater than 64 characters"
    url = ReadConfig.get_registration_url()
    page_name = "User Registration Page"

    def __init__(self, driver: webdriver):
        self.driver = driver

    def select_gender(self, gender: str):
        if len(gender) > 1:
            gender = gender[0]
        gender = gender.lower()
        if gender == "m":
            self.driver.find_element(By.ID, self.gender_male_selection_id).click()
        else:
            self.driver.find_element(By.ID, self.gender_female_seelction_id).click()

    def verify_gender_selection(self, gender: str):
        if len(gender) > 1:
            gender = gender[0]
        gender = gender.lower()
        if gender == "m":
            selected_gender = self.driver.find_element(By.ID, self.gender_male_selection_id)
        else:
            selected_gender = self.driver.find_element(By.ID, self.gender_female_seelction_id)
        if selected_gender.is_selected():
            return True
        return False

    def enter_first_name(self, name: str):
        first_name_field = self.driver.find_element(By.ID, self.first_name_field_id)
        first_name_field.send_keys(name)

    def enter_last_name(self, name: str):
        last_name_field = self.driver.find_element(By.ID, self.last_name_field_id)
        last_name_field.send_keys(name)

    def enter_email(self, email: str):
        email_field = self.driver.find_element(By.ID, self.email_field_id)
        email_field.send_keys(email)

    def enter_company_name(self, company: str):
        company_field = self.driver.find_element(By.ID, self.company_field_id)
        company_field.send_keys(company)

    def check_newsletter_box(self):
        newsletter_checkbox = self.driver.find_element(By.ID, self.newsletter_id)
        newsletter_checkbox.click()

    def enter_password(self, password: str):
        password_field = self.driver.find_element(By.ID, self.password_id)
        password_field.send_keys(password)

    def enter_confirm_password(self, password: str):
        confirm_pw_field = self.driver.find_element(By.ID, self.confirm_password_id)
        confirm_pw_field.send_keys(password)

    def click_register(self):
        register_button = self.driver.find_element(By.ID, self.register_button_id)
        register_button.click()