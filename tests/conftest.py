import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="session", autouse=True)
def browser_set():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = "eager"
    browser.config.driver_options = driver_options
    browser.config.base_url= "https://demoqa.com"
    browser.driver.set_window_size(1920, 1080)

    yield
    browser.quit()