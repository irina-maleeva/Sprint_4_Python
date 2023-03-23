import allure
from pages.home_page import HomePage
from pages.order_page import OrderPage
from pages.yandex_page import YandexPage

url = 'https://qa-scooter.praktikum-services.ru/'

@allure.title('Проверка перехода на главную страницу по клику на лого "Самокат"')
@allure.description('Будучи на странице заказа, нажать на лого "Самокат" и убедиться, что произошел переход на главную страницу')
def test_samokat_logo_link(driver):
    home_page = HomePage(driver)
    home_page.click_order_button_in_heading()
    order_page = OrderPage(driver)
    order_page.wait_for_page_load()
    assert driver.current_url == url + 'order'
    order_page.click_samokat_logo()
    assert driver.current_url == url

@allure.title('Проверка перехода на главную страницу Яндекс.дзен по клику на лого "Яндекс"')
@allure.description('Будучи на странице заказа, нажать на лого "Яндекс" и убедиться, что произошел переход на главную страницу Яндекс.дзен')
def test_yandex_logo_link(driver):
    home_page = HomePage(driver)
    home_page.click_order_button_in_heading()
    order_page = OrderPage(driver)
    order_page.wait_for_page_load()
    assert driver.current_url == url + 'order'
    order_page.click_yandex_logo()
    yandex_page = YandexPage(driver)
    yandex_page.wait_for_second_tab()
    driver.switch_to.window(driver.window_handles[1])
    yandex_page.wait_for_page_load()
    assert driver.current_url == 'https://dzen.ru/?yredirect=true'