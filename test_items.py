link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_basket_btn(browser):
    browser.get(link)
    basket_btn = browser.find_element_by_xpath("//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    if basket_btn:
        assert True
    else:
        assert False, \
            f"Test {basket_btn} failed! No 'add to basket' button on the page"
