import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

from pages.registration_page import RegistrationPage
from pages.auth_page_with_password import FullAuthPage
from pages.auth_page_with_code import AuthWithCodePage
from pages.pwd_recovery_page import PasswordRecoveryPage


@pytest.fixture(scope="session")
def browser():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    options = Options()
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver

    driver.quit()


@pytest.fixture(scope="session")
def reg_page(browser):
    reg_page = RegistrationPage(browser)
    return reg_page


@pytest.fixture(scope="session")
def auth_with_password_page(browser):
    auth_with_password_page = FullAuthPage(browser)
    return auth_with_password_page


@pytest.fixture(scope="session")
def auth_with_code_page(browser):
    auth_with_code_page = AuthWithCodePage(browser)
    return auth_with_code_page


@pytest.fixture(scope="session")
def pwd_recovery_page(browser):
    pwd_recovery_page = PasswordRecoveryPage(browser)
    return pwd_recovery_page
