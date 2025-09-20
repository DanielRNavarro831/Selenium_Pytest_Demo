from selenium import webdriver
from selenium.webdriver.common.by import By


class AdminDashboard:
    dashboard_page_title = "Dashboard / nopCommerce administration"
    page_name = "Admin Dashboard"

    def __init__(self, driver: webdriver):
        self.driver = driver

    def logout(self):
        logout_button = self.driver.find_element(By.LINK_TEXT, "Logout")
        logout_button.click()
