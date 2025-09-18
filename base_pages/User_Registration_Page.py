from selenium import webdriver
from selenium.webdriver.common.by import By


class UserRegistrationPage:

    def __init__(self, driver: webdriver):
        self.driver = driver

