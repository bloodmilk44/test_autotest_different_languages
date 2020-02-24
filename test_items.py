link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
import time


def test_different_languages_button(browser):
    browser.get(link)
    time.sleep(5)
    assert browser.find_element_by_class_name('btn-add-to-basket').is_displayed(), \
        'Кнопка добавления товара в корзину отсутсвует'
