import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class YandexPage:

    dzen_logo = [By.XPATH, './/span[@aria-label="Логотип Дзен"]']

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Дождаться открытия второй вкладки браузера')
    def wait_for_second_tab(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.number_of_windows_to_be(2))

    @allure.step('Дождаться загрузки страницы Яндекс.Дзен')
    def wait_for_page_load(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.dzen_logo))