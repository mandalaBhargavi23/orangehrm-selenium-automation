from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_valid_login(driver):
    login = LoginPage(driver)
    login.open()
    login.login("Admin", "admin123")

    dashboard = DashboardPage(driver)
    assert dashboard.is_dashboard_displayed()


def test_invalid_login(driver):
    login = LoginPage(driver)
    login.open()
    login.login("invalid_user", "invalid_password")

    assert "Invalid credentials" in login.get_error_message()


def test_logout(driver):
    login = LoginPage(driver)
    login.open()
    login.login("Admin", "admin123")

    dashboard = DashboardPage(driver)
    dashboard.logout()

    assert "auth/login" in driver.current_url
