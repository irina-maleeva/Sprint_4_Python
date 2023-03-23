import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class RentDetailsForm:
    details_form_heading = [By.XPATH, '//div[text()="Про аренду"]']
    date_input_field = [By.XPATH, './/input[@placeholder="* Когда привезти самокат"]']
    rent_duration_dropdown_options = [By.XPATH, './/div[@class="Dropdown-option"]']
    rent_duration_input_field = [By.XPATH, './/div[@class="Dropdown-root"]']
    black_color_checkbox = [By.ID, 'black']
    grey_color_checkbox = [By.ID, 'grey']
    comment_input_field = [By.XPATH, './/input[@placeholder="Комментарий для курьера"]']
    order_button = [By.XPATH, './/div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]']

    def __init__(self, driver):
        self.driver = driver

    def wait_for_page_load(self):
        WebDriverWait(self.driver, 13).until(
            expected_conditions.visibility_of_element_located(self.details_form_heading))

    def choose_date(self, date):
        self.driver.find_element(*self.date_input_field).send_keys(date)
        self.driver.find_element(*self.date_input_field).send_keys(Keys.ENTER)

    def choose_rent_duration(self):
        self.driver.find_element(*self.rent_duration_input_field).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.rent_duration_dropdown_options))
        self.driver.find_elements(*self.rent_duration_dropdown_options)[random.randint(0, 6)].click()

    def choose_grey_color(self):
        self.driver.find_element(*self.grey_color_checkbox).click()

    def choose_black_color(self):
        self.driver.find_element(*self.black_color_checkbox).click()

    def write_comment(self, comment):
        self.driver.find_element(*self.comment_input_field).send_keys(comment)

    def click_order_button(self):
        self.driver.find_element(*self.order_button).click()
