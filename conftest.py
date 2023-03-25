import pytest
from selenium import webdriver

url = 'https://qa-scooter.praktikum-services.ru/'

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get(url)
    yield driver
    driver.quit()

@pytest.fixture()
def driver_ME():
    driver = webdriver.Edge()
    driver.get(url)
    yield driver
    driver.quit()