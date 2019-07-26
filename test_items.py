def test_guest_should_see_login_link(browser):
    assert browser.find_element_by_class_name("btn-add-to-basket")
