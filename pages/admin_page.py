from selenium.webdriver.common.by import By


class AdminPage:
    ADMIN_TITLE = (By.XPATH, "//h6[normalize-space()='User Management']")

    def __init__(self, driver):
        self.driver = driver

    def is_admin_page_displayed(self):
        return self.driver.find_element(*self.ADMIN_TITLE).is_displayed()
