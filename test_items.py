import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_in_es_language(browser):
    browser.get(link)
    btn = browser.find_element_by_css_selector('.btn-add-to-basket').text

    assert btn == 'Añadir al carrito', 'Button is not finded'
