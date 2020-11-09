import time

def test_check_basket_button_exists(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    basket_btn_xpath = "//button[@class='btn btn-lg btn-primary btn-add-to-basket']"

    def is_element_present(browser):
        try:
            browser.implicitly_wait(5)
            browser.find_element_by_xpath(basket_btn_xpath)
            return True
        except:
            return False

    assert is_element_present(browser) == True, \
        f"Test has failed! No {basket_btn_xpath} button on the page"
