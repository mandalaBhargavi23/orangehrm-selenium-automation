from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PimPage


def login_to_application(driver):
    login = LoginPage(driver)
    login.open()
    login.login("Admin", "admin123")


def test_open_add_employee(driver):
    login_to_application(driver)

    dashboard = DashboardPage(driver)
    dashboard.open_pim()

    pim = PimPage(driver)
    pim.click_add()

    assert "pim/addEmployee" in driver.current_url


def test_add_employee_form_submission(driver):
    login_to_application(driver)

    dashboard = DashboardPage(driver)
    dashboard.open_pim()

    pim = PimPage(driver)
    pim.click_add()
    pim.add_employee("Test", "Automation", "User")

    assert "pim" in driver.current_url


def test_employee_list_search(driver):
    login_to_application(driver)

    dashboard = DashboardPage(driver)
    dashboard.open_pim()

    pim = PimPage(driver)
    pim.open_employee_list()
    pim.search_by_employee_id("123")

    assert "pim/viewEmployeeList" in driver.current_url
