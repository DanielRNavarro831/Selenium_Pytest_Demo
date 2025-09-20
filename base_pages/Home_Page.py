from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.read_properties import ReadConfig
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    register_button_class = "ico-register"
    login_button_class = "ico-login"
    wishlist_button_class = "ico-wishlist"
    shopping_cart_button_class = "ico-cart"
    search_field_id = "small-searchterms"
    search_submit_css_selector = ".search-box-button"
    currency_dropdown_id = "customerCurrency"
    price_check_xpath = "//span[@class='price actual-price']"
    top_menu_xpath = '//ul[@class="top-menu notmobile"]/li'
    url = ReadConfig.get_store_home_url()
    page_name = "Home Page"

    def __init__(self, driver: webdriver):
        self.driver = driver

    def get_top_menu_xpath(self, category: str):
        category = category.lower()
        categories = {"computers": 1, "electronics": 2, "apparel": 3, "digital downloads": 4, "books": 5, "jewelry": 6,
                      "gift cards": 7}
        selected_category = categories[category]
        return f'{self.top_menu_xpath}[{selected_category}]'

########################################################################################################################
# Header
########################################################################################################################
    def click_register(self):
        register_button = self.driver.find_element(By.CLASS_NAME, self.register_button_class)
        register_button.click()

    def click_login(self):
        login_button = self.driver.find_element(By.CLASS_NAME, self.login_button_class)
        login_button.click()

    def click_wishlist(self):
        wishlist_button = self.driver.find_element(By.CLASS_NAME, self.wishlist_button_class)
        wishlist_button.click()

    def click_shopping_cart(self):
        shopping_cart = self.driver.find_element(By.CLASS_NAME, self.shopping_cart_button_class)
        shopping_cart.click()

    def click_currency_dropdown(self, selection: str):
        dropdown = Select(self.driver.find_element(By.ID, self.currency_dropdown_id))
        dropdown.select_by_visible_text(selection)

    def check_currency(self):
        price_text = self.driver.find_element(By.XPATH, self.price_check_xpath).text
        if "$" in price_text:
            return "US Dollar"
        return "Euro"

########################################################################################################################
# Search Bar
########################################################################################################################
    def enter_searchbox(self, searchterms: str):
        searchbox = self.driver.find_element(By.ID, self.search_field_id)
        searchbox.send_keys(searchterms)
        search_submit = self.driver.find_element(By.CSS_SELECTOR, self.search_submit_css_selector)
        search_submit.click()

########################################################################################################################
# Top Menu
########################################################################################################################

    def click_computers(self, submenu=None):
        wait = WebDriverWait(self.driver, 10)
        xpath = self.get_top_menu_xpath("computers")
        if submenu:
            computers_link = self.driver.find_element(By.XPATH, xpath)
            actions = ActionChains(self.driver)
            actions.move_to_element(computers_link).perform()
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, submenu)))
            self.driver.find_element(By.LINK_TEXT, submenu).click()
        else:
            computers_link = self.driver.find_element(By.XPATH, xpath)
            computers_link.click()

