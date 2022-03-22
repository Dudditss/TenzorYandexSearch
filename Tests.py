from YandexPages import SearchHelper


def test_yandex_search(browser):
    # Запускаем тест
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()

    # Работаем с поисковой строкой
    yandex_main_page.enter_word("тензор")

    # Проверка на наличие подсказок под полем ввода
    elements_suggest = yandex_main_page.suggest_exam()
    assert len(elements_suggest) > 0

    # Нажимаем на поисковую кнопку
    yandex_main_page.click_on_the_search_button()

    # Проверяем количество ссылок на tensor.ru
    search_elements = yandex_main_page.search_result()   # Проверяем количество ссылок на tensor.ru
    if search_elements[0].count('tensor.ru') >= 5:
        print('В первых 5 результатах есть ссылка на tensor.ru')
    else:
        print("В первых 5 результатах нет ссылки на 'tensor.ru', всего результатов:", str(search_elements[0].count('tensor.ru')))
