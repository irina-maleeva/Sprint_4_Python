import pytest
import allure
import datetime

from pages.home_page import HomePage
from pages.order_page import OrderPage
from pages.rent_details import RentDetailsForm

current_date = datetime.datetime.today()
tomorrow = (current_date + datetime.timedelta(days=1)).strftime('%d.%m.%Y')
day_after_tomorrow = (current_date + datetime.timedelta(days=2)).strftime('%d.%m.%Y')
url = 'https://qa-scooter.praktikum-services.ru/'

@allure.title('Заказ самоката - вход через кнопку "Заказать" в шапке страницы- позитивный сценарий')
@allure.description('Проверка позитивного сценария заказа самоката с корректным заполнением всех полей формы')
@pytest.mark.parametrize('name, family_name, address, metro, phone, date, comment',
                             [['Ян', 'Ли', '3-я улица Ямского поля, 6', 'Черкизовская', '+79160000002', tomorrow, 'Позвоните мне'],
                              ['Яна', 'Рождественская', 'Зубовский бульвар, 5', 'Преображенская площадь', '+791600000027', day_after_tomorrow, 'Лучше стучать']])
def test_order_via_button_in_header_correct_data(driver_ME, name, family_name, address, metro, phone, date, comment):
    home_page = HomePage(driver_ME)
    home_page.click_order_button_in_heading()

    order_page = OrderPage(driver_ME)
    order_page.wait_for_page_load()
    order_page.fill_in_name_field(name)
    order_page.fill_in_family_name_field(family_name)
    order_page.fill_in_address_field(address)
    order_page.choose_metro_station(metro)
    order_page.fill_in_phone_number(phone)
    order_page.click_submit_button()

    rent_details_form = RentDetailsForm(driver_ME)
    rent_details_form.wait_for_page_load()

    rent_details_form.choose_date(date)
    rent_details_form.choose_rent_duration()
    rent_details_form.choose_grey_color()
    rent_details_form.write_comment(comment)
    rent_details_form.click_order_button()

    order_page.click_yes_button()
    order_page.wait_confirmation()
    assert 'Заказ оформлен' in order_page.get_confirmation_heading_text()

@allure.title('Заказ самоката - вход через кнопку "Заказать" внизу страницы- позитивный сценарий')
@allure.description('Проверка позитивного сценария заказа самоката через кнопку внизу страницы с корректным заполнением всех полей формы, кроме поля "Комментарий"')
@pytest.mark.parametrize('name, family_name, address, metro, phone, date',
                             [['Роман', 'Александровский', 'Новомытищенский проспект, 33, корпус 1', 'Перово', '+12345678901', tomorrow],
                              ['Аркадий', 'Петров', 'Тверская, 5', 'Сокол', '+791600006627', day_after_tomorrow]])
def test_order_via_button_in_bottom_and_check_link(driver, name, family_name, address, metro, phone, date):
    home_page = HomePage(driver)
    home_page.accept_cookies()
    home_page.click_order_button_in_bottom()

    order_page = OrderPage(driver)
    order_page.wait_for_page_load()
    order_page.fill_in_name_field(name)
    order_page.fill_in_family_name_field(family_name)
    order_page.fill_in_address_field(address)
    order_page.choose_metro_station(metro)
    order_page.fill_in_phone_number(phone)
    order_page.click_submit_button()

    rent_details_form = RentDetailsForm(driver)
    rent_details_form.wait_for_page_load()

    rent_details_form.choose_date(date)
    rent_details_form.choose_rent_duration()
    rent_details_form.choose_black_color()
    rent_details_form.click_order_button()

    order_page.click_yes_button()
    order_page.wait_confirmation()
    assert 'Заказ оформлен' in order_page.get_confirmation_heading_text()