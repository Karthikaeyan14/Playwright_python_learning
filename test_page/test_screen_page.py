import pytest
from playwright.sync_api import expect,Page
from pageobjectmodel.login import login
from pageobjectmodel.screen_page import Screen

@pytest.mark.valid_product
def test_valid_product(page:Page):
    login_page=login(page)
    login_page.navigation()
    login_page.enter_username("karthi1412@gmail.com","KARTHIKAEYANr@14")
    login_page.login_click()
    expect(page).to_have_url("https://rahulshettyacademy.com/client/#/dashboard/dash")
    screen=Screen(page)
    screen.search_product('ZARA COAT 3')
    print(screen.valid_product())

@pytest.mark.invalid_product
def test_invalid_product(page:Page):
    login_page=login(page)
    login_page.navigation()
    login_page.enter_username("karthi1412@gmail.com","KARTHIKAEYANr@14")
    login_page.login_click()
    expect(page).to_have_url("https://rahulshettyacademy.com/client/#/dashboard/dash")
    screen=Screen(page)
    screen.search_product('ab')
    #screen.search_product().press("Enter")
    expect(screen.no_product()).to_be_visible()
    text=screen.no_product().text_content()
    assert text ==' No Products Found '

@pytest.mark.valid_price
def test_search_valid_price(page:Page):
    login_page=login(page)
    login_page.navigation()
    login_page.enter_username("karthi1412@gmail.com","KARTHIKAEYANr@14")
    login_page.login_click()
    expect(page).to_have_url("https://rahulshettyacademy.com/client/#/dashboard/dash")
    screen=Screen(page)
    screen.price_range('2200','55000')
    print(screen.valid_product())



@pytest.mark.add_product
def test_add_product(page:Page):
    login_page=login(page)
    login_page.navigation()
    login_page.enter_username("karthi1412@gmail.com","KARTHIKAEYANr@14")
    login_page.login_click()
    expect(page).to_have_url("https://rahulshettyacademy.com/client/#/dashboard/dash")
    screen=Screen(page)
    screen.search_product('ZARA COAT 3')
    screen.click_add()
    expect(screen.message_occur()).to_be_visible()
