import pytest
import allure
import datetime
from dataclasses import dataclass
from pages.home_page import HomePage
from pages.order_page import OrderPage
from pages.order_page import TestData as _TestData

current_date = datetime.datetime.today()
tomorrow = (current_date + datetime.timedelta(days=1)).strftime('%d.%m.%Y')
day_after_tomorrow = (current_date + datetime.timedelta(days=2)).strftime('%d.%m.%Y')
url = 'https://qa-scooter.praktikum-services.ru/'

testDataSet_1 = _TestData('Ян', 'Ли', '3-я улица Ямского поля, 6', 'Черкизовская', '+79160000002', tomorrow,
                         'Позвоните мне')
testDataSet_2 = _TestData('Яна', 'Рождественская', 'Зубовский бульвар, 5', 'Преображенская площадь', '+791600000027',
                         day_after_tomorrow, 'Лучше стучать')
testDataSet_3 = _TestData('Роман', 'Александровский', 'Новомытищенский проспект, 33, корпус 1', 'Перово', '+12345678901', tomorrow, '')
testDataSet_4 = _TestData('Аркадий', 'Петров', 'Тверская, 5', 'Сокол', '+791600006627', day_after_tomorrow, '')

@allure.title('Заказ самоката - вход через кнопку "Заказать" в шапке страницы- позитивный сценарий')
@allure.description('Проверка позитивного сценария заказа самоката с корректным заполнением всех полей формы')
@pytest.mark.parametrize('testDataSet',
                             [testDataSet_1, testDataSet_2])
def test_order_via_button_in_header_correct_data(driver_ME, testDataSet):
    home_page = HomePage(driver_ME)
    home_page.click_order_button_in_heading()

    order_page = OrderPage(driver_ME)
    order_page.wait_for_page_load()
    order_page.fill_first_form_fields(testDataSet)
    order_page.click_submit_button()
    order_page.wait_for_details_form_load()
    order_page.choose_date(testDataSet.date)
    order_page.choose_rent_duration()
    order_page.choose_grey_color()
    order_page.write_comment(testDataSet.comment)
    order_page.click_order_button()
    order_page.click_yes_button()
    order_page.wait_confirmation()
    assert 'Заказ оформлен' in order_page.get_confirmation_heading_text()

@allure.title('Заказ самоката - вход через кнопку "Заказать" внизу страницы- позитивный сценарий')
@allure.description('Проверка позитивного сценария заказа самоката через кнопку внизу страницы с корректным заполнением всех полей формы, кроме поля "Комментарий"')
@pytest.mark.parametrize('testDataSet',
                             [testDataSet_3, testDataSet_4])
def test_order_via_button_in_bottom_and_check_link(driver_ME, testDataSet):
    home_page = HomePage(driver_ME)
    home_page.accept_cookies()
    home_page.click_order_button_in_bottom()

    order_page = OrderPage(driver_ME)
    order_page.wait_for_page_load()
    order_page.fill_first_form_fields(testDataSet)
    order_page.click_submit_button()
    order_page.wait_for_details_form_load()
    order_page.choose_date(testDataSet.date)
    order_page.choose_rent_duration()
    order_page.choose_black_color()
    order_page.write_comment(testDataSet.comment)
    order_page.click_order_button()
    order_page.click_yes_button()
    order_page.wait_confirmation()
    assert 'Заказ оформлен' in order_page.get_confirmation_heading_text()