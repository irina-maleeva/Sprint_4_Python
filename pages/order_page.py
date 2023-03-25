import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class OrderPage:
    path = 'order'
    form_heading = [By.XPATH, '//div[text()="Для кого самокат"]']
    name_input_field = [By.XPATH, './/input[@placeholder="* Имя"]']
    family_name_input_field = [By.XPATH, './/input[@placeholder="* Фамилия"]']
    address_input_field = [By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]']
    metro_station_input_field = [By.XPATH, './/input[@placeholder="* Станция метро"]']
    dropdown_metro_stations = [By.XPATH, '//div[@class="select-search__select"]/ul/li']
    metro_option = [By.XPATH, './/div[@class="select-search__select][1]']
    phone_input_field = [By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]']
    submit_button = [By.XPATH, '//button[text()= "Далее"]']
    order_created_message = [By.XPATH, './/div[text()="Заказ оформлен"]']
    samokat_logo = [By.XPATH, './/img[@alt="Scooter"]']
    yandex_logo = [By.XPATH, './/img[@alt="Yandex"]']
    yes_button = [By.XPATH, './/button[text()="Да"]']

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Подождать загрузки страницы заказа')
    def wait_for_page_load(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.form_heading))

    @allure.step('Заполнить поле "Имя"')
    def fill_in_name_field(self, name):
        self.driver.find_element(*self.name_input_field).send_keys(name)

    @allure.step('Заполнить поле "Фамилия"')
    def fill_in_family_name_field(self, family_name):
        self.driver.find_element(*self.family_name_input_field).send_keys(family_name)

    @allure.step('Заполнить поле "Адрес"')
    def fill_in_address_field(self, address):
        self.driver.find_element(*self.address_input_field).send_keys(address)

    @allure.step('Выбрать станцию метро из выпадающего списка, напечатав ее название в поле ввода')
    def choose_metro_station(self, metro_station):
        self.driver.find_element(*self.metro_station_input_field).send_keys(metro_station)
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.dropdown_metro_stations))
        self.driver.find_element(*self.dropdown_metro_stations).click()

    @allure.step('Заполнить поле "Номер телефона"')
    def fill_in_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_input_field).send_keys(phone_number)

    @allure.step('Нажать кнопку "Далее"')
    def click_submit_button(self):
        self.driver.find_element(*self.submit_button).click()

    @allure.step('Подождать появление всплывающего окна с сообщением об успешном создании заказа')
    def wait_confirmation(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located(self.order_created_message))

    @allure.step('Получить текст всплывающего окна "Заказ оформлен"')
    def get_confirmation_heading_text(self):
        return self.driver.find_element(*self.order_created_message).text

    @allure.step('Нажать на логотип "Самокат"')
    def click_samokat_logo(self):
        self.driver.find_element(*self.samokat_logo).click()

    @allure.step('Нажать на логотип "Яндекс"')
    def click_yandex_logo(self):
        self.driver.find_element(*self.yandex_logo).click()

    @allure.step('Нажать на кнопку "Да" в форме "Хотите оформить заказ?')
    def click_yes_button(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.yes_button))
        self.driver.find_element(*self.yes_button).click()