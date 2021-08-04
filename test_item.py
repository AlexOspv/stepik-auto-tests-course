import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_can_add_some_stuff(browser):
    browser.get(link)
    time.sleep(5)
    assert browser.find_elements_by_css_selector("button.btn-add-to-basket") is not None, "Button is missing"