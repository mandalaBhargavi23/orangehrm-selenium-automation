from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage


def login_to_application(driver):
    login = LoginPage(driver)
    login.open()
    login.login("Admin", "admin123")


def test_admin_navigation(driver):
    login_to_application(driver)

    dashboard = DashboardPage(driver)
    dashboard.open_admin()

    admin = AdminPage(driver)
    assert admin.is_admin_page_displayed()


def test_pim_navigation(driver):
    login_to_application(driver)

    dashboard = DashboardPage(driver)
    dashboard.open_pim()

    assert "pim" in driver.current_url


def test_leave_navigation(driver):
    login_to_application(driver)

    dashboard = DashboardPage(driver)
    dashboard.open_leave()

    assert "leave" in driver.current_url
