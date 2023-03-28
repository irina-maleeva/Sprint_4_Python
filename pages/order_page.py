import allure
import random
from dataclasses import dataclass
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

@dataclass()
class TestData:
    name: str
    family_name: str
    address: str
    metro: str
    phone: str
    date: str
    comment: str


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

    details_form_heading = [By.XPATH, '//div[text()="Про аренду"]']
    date_input_field = [By.XPATH, './/input[@placeholder="* Когда привезти самокат"]']
    rent_duration_dropdown_options = [By.XPATH, './/div[@class="Dropdown-option"]']
    rent_duration_input_field = [By.XPATH, './/div[@class="Dropdown-root"]']
    black_color_checkbox = [By.ID, 'black']
    grey_color_checkbox = [By.ID, 'grey']
    comment_input_field = [By.XPATH, './/input[@placeholder="Комментарий для курьера"]']
    order_button = [By.XPATH, './/div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]']

    order_created_message = [By.XPATH, './/div[text()="Заказ оформлен"]']
    samokat_logo = [By.XPATH, './/img[@alt="Scooter"]']
    yandex_logo = [By.XPATH, './/img[@alt="Yandex"]']
    yes_button = [By.XPATH, './/button[text()="Да"]']

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Подождать загрузки страницы заказа')
    def wait_for_page_load(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.form_heading))

    @allure.step('Заполнить поля формы')
    def fill_first_form_fields(self, testData):
        self.driver.find_element(*self.name_input_field).send_keys(testData.name)
        self.driver.find_element(*self.family_name_input_field).send_keys(testData.family_name)
        self.driver.find_element(*self.address_input_field).send_keys(testData.address)
        self.driver.find_element(*self.metro_station_input_field).send_keys(testData.metro)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.dropdown_metro_stations))
        self.driver.find_element(*self.dropdown_metro_stations).click()
        self.driver.find_element(*self.phone_input_field).send_keys(testData.phone)


    @allure.step('Нажать кнопку "Далее"')
    def click_submit_button(self):
        self.driver.find_element(*self.submit_button).click()

    @allure.step('Подождать загрузки формы "Про аренду"')
    def wait_for_details_form_load(self):
        WebDriverWait(self.driver, 13).until(
            expected_conditions.visibility_of_element_located(self.details_form_heading))

    @allure.step('Выбрать дату')
    def choose_date(self, date):
        self.driver.find_element(*self.date_input_field).send_keys(date)
        self.driver.find_element(*self.date_input_field).send_keys(Keys.ENTER)

    @allure.step('Выбрать длительность аренды')
    def choose_rent_duration(self):
        self.driver.find_element(*self.rent_duration_input_field).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.rent_duration_dropdown_options))
        self.driver.find_elements(*self.rent_duration_dropdown_options)[random.randint(0, 6)].click()

    @allure.step('Выбрать серый цвет')
    def choose_grey_color(self):
        self.driver.find_element(*self.grey_color_checkbox).click()

    @allure.step('Выбрать черный цвет')
    def choose_black_color(self):
        self.driver.find_element(*self.black_color_checkbox).click()

    @allure.step('Написать комментарий')
    def write_comment(self, comment):
        self.driver.find_element(*self.comment_input_field).send_keys(comment)

    @allure.step('Нажать кнопку "Заказать"')
    def click_order_button(self):
        self.driver.find_element(*self.order_button).click()



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


