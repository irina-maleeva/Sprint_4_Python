import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get('https://qa-scooter.praktikum-services.ru/')
    yield driver
    driver.quit()

@pytest.fixture()
def driver_ME():
    driver = webdriver.Edge()
    driver.get('https://qa-scooter.praktikum-services.ru/')
    yield driver
    driver.quit()