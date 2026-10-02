from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PimPage:
    ADD_BUTTON = (By.XPATH, "//button[normalize-space()='Add']")
    FIRST_NAME = (By.NAME, "firstName")
    MIDDLE_NAME = (By.NAME, "middleName")
    LAST_NAME = (By.NAME, "lastName")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")
    EMPLOYEE_LIST = (By.XPATH, "//a[normalize-space()='Employee List']")
    SEARCH_EMPLOYEE_ID = (
        By.XPATH,
        "(//input[contains(@class,'oxd-input')])[2]"
    )
    SEARCH_BUTTON = (By.XPATH, "//button[normalize-space()='Search']")
    RESET_BUTTON = (By.XPATH, "//button[normalize-space()='Reset']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_add(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_BUTTON)).click()

    def add_employee(self, first_name, middle_name, last_name):
        self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        ).send_keys(first_name)
        self.driver.find_element(*self.MIDDLE_NAME).send_keys(middle_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.SAVE_BUTTON).click()

    def open_employee_list(self):
        self.wait.until(EC.element_to_be_clickable(self.EMPLOYEE_LIST)).click()

    def search_by_employee_id(self, employee_id):
        field = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_EMPLOYEE_ID)
        )
        field.send_keys(employee_id)
        self.driver.find_element(*self.SEARCH_BUTTON).click()

    def reset_search(self):
        self.driver.find_element(*self.RESET_BUTTON).click()
