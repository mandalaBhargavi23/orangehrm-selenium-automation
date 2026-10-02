# OrangeHRM Selenium Automation Framework

A web automation testing project for the OrangeHRM demo application using **Python, Selenium WebDriver and PyTest**.

## Application

OrangeHRM Open Source Demo:

https://opensource-demo.orangehrmlive.com/

Demo credentials:

- Username: `Admin`
- Password: `admin123`

> The demo website can change over time. If a locator or workflow changes, update the corresponding Page Object.

## Technologies

- Python
- Selenium WebDriver
- PyTest
- PyTest HTML
- Page Object Model (POM)
- XPath
- CSS Selectors

## Automated Modules

### Authentication
- Valid login
- Invalid login
- Logout

### Navigation
- Admin module
- PIM module
- Leave module

### Employee Management
- Open Add Employee
- Add employee form submission
- Employee list
- Employee ID search

## Project Structure

```text
orangehrm-selenium-automation/
│
├── pages/
│   ├── login_page.py
│   ├── dashboard_page.py
│   ├── admin_page.py
│   └── pim_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_navigation.py
│   └── test_employee.py
│
├── utils/
│   └── driver_setup.py
│
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md
```

## Setup

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run all tests:

```bash
pytest
```

Generate an HTML report:

```bash
pytest --html=reports/report.html --self-contained-html
```

## Framework Approach

The project follows the **Page Object Model**. Locators and page actions are maintained in page classes, while test files contain the actual test scenarios and assertions.

## QA Concepts Demonstrated

- Functional testing
- Positive testing
- Negative testing
- Regression test automation
- UI validation
- Navigation testing
- Form validation
- Web element identification
- XPath and CSS selectors
- Explicit waits
- PyTest fixtures
- Assertions
- HTML test reporting

## Future Enhancements

- Add employee edit/delete automation
- Add data-driven testing
- Add screenshot capture on failure
- Add logging
- Add GitHub Actions CI
- Add cross-browser execution
- Add more negative test scenarios

## Author

Add your name and GitHub profile here.
