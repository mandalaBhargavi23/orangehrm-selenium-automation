from selenium.webdriver.common.by import By


class DashboardPage:
    DASHBOARD_TITLE = (By.XPATH, "//h6[normalize-space()='Dashboard']")
    ADMIN_MENU = (By.XPATH, "//span[normalize-space()='Admin']")
    PIM_MENU = (By.XPATH, "//span[normalize-space()='PIM']")
    LEAVE_MENU = (By.XPATH, "//span[normalize-space()='Leave']")
    USER_MENU = (By.CSS_SELECTOR, ".oxd-userdropdown-tab")
    LOGOUT_LINK = (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver = driver

    def is_dashboard_displayed(self):
        return self.driver.find_element(*self.DASHBOARD_TITLE).is_displayed()

    def open_admin(self):
        self.driver.find_element(*self.ADMIN_MENU).click()

    def open_pim(self):
        self.driver.find_element(*self.PIM_MENU).click()

    def open_leave(self):
        self.driver.find_element(*self.LEAVE_MENU).click()

    def logout(self):
        self.driver.find_element(*self.USER_MENU).click()
        self.driver.find_element(*self.LOGOUT_LINK).click()
