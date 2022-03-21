from BaseApp import BasePage
from selenium.webdriver.common.by import By
import time


class YandexSearchLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")  # Локатор поля поиска
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")  # Локатор кнопки поиска
    LOCATOR_YANDEX_SUGGEST = (By.XPATH, "/html/body/div[2]")  # Локатор таблицы подсказок
    LOCATOR_YANDEX_SEARCH_RESULTS = (By.ID, "search-result")  # Локатор таблицы подсказок


class SearchHelper(BasePage):

    def enter_word(self, word):  # Функция проверки строки поиска
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD, time=10)
        search_field.click()
        search_field.send_keys(word)
        time.sleep(1)
        return search_field

    def click_on_the_search_button(self):  # Функция нажатия кнопки поиска
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_BUTTON, time=10).click()

    def suggest_exam(self):  # Функция получения элементов поля подсказок
        suggest_list = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_SUGGEST, time=10)
        suggest = [x.text for x in suggest_list if len(x.text) > 0]
        return suggest

    def search_result(self):  # Функция получения результатов поиска
        result_list = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_RESULTS, time=10)
        result = [x.text for x in result_list if len(x.text) > 0]
        return result
