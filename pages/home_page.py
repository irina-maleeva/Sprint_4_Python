import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class HomePage:

    order_button_in_header = [By.XPATH, '//div[@class = "Header_Nav__AGCXC"]/button[text()="Заказать"]']
    order_button_in_lower_part = [By.XPATH, '//div[@class="Home_ThirdPart__LSTEE"]//button[text()="Заказать"]']
    main_page_message_part = [By.XPATH, './/div[text() ="Привезём его прямо к вашей двери,"']
    questions_section_head = [By.XPATH, './/div[text()="Вопросы о важном"]']
    questions = [By.CLASS_NAME, 'accordion__heading']
    visible_answer = [By.XPATH, './/div[contains(@class, "accordion__panel") and not(@hidden)]']
    accept_cookies_button = [By.XPATH, './/button[text()="да все привыкли"]']

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Прокрутить страницу до раздела "Вопросы о важном"')
    def scroll_to_questions_section(self):
        questions_section = self.driver.find_element(*self.questions_section_head)
        self.driver.execute_script('arguments[0].scrollIntoView();', questions_section)

    @allure.step('Нажать на вопрос номер {number}')
    def click_question(self, number):
        questions = self.driver.find_elements(*self.questions)
        questions[number-1].click()

    @allure.step('Проверить что открывшийся текст ответа совпадает с ожидаемым')
    def check_answer(self, text_answer):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.visible_answer))
        assert self.driver.find_element(*self.visible_answer).text == text_answer

    @allure.step('Нажать кнопку "Заказать" в шапке страницы')
    def click_order_button_in_heading(self):
        self.driver.find_element(*self.order_button_in_header).click()

    @allure.step('Нажать кнопку принятия cookies')
    def accept_cookies(self):
        self.driver.find_element(*self.accept_cookies_button).click()

    @allure.step('Нажать кнопку "Заказать" внизу страницы')
    def click_order_button_in_bottom(self):
        self.driver.find_element(*self.order_button_in_lower_part).click()

    @allure.step('Подождать загрузки страницы')
    def wait_for_page_load(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.main_page_message_part))