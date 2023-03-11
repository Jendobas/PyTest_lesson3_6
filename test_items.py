from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_shopping_cart(browser):
    browser.get(link)
    browser.implicitly_wait(3)
    button = browser.find_element(By.CLASS_NAME, "btn-lg.btn-add-to-basket")

    assert button, 'button not found'
