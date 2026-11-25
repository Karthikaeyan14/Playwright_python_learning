import pytest
from pageobjectmodel.login import login
from pageobjectmodel.screen_page import Screen
from playwright.sync_api import Page, expect



@pytest.mark.valid_login_details
def test_valid(page:Page):
    login_page=login(page)
    login_page.navigation()
    login_page.enter_username("karthi1412@gmail.com","KARTHIKAEYANr@14")
    login_page.login_click()
    expect(page).to_have_url("https://rahulshettyacademy.com/client/#/dashboard/dash")


@pytest.mark.invalid_login_details
def test_invalid(page:Page):
    
    login_page=login(page)
    login_page.navigation()
    login_page.enter_username("karthi1412@gmail.com","learning1")
    login_page.login_click()
    expect(login_page.error()).to_be_visible()
    #(login_page.error())

@pytest.mark.empty_login_details
def test_empty(page:Page):  
    login_page=login(page)
    login_page.navigation()
    login_page.enter_username("","")
    login_page.login_click()
    expect(login_page.email_requried()).to_be_visible()
    expect(login_page.password_required()).to_be_visible()


@pytest.mark.invalid_email_details
def test_invalid_email(page:Page):
    login_page=login(page)
    login_page.navigation()
    login_page.enter_username("karthi","learning")
    login_page.login_click()
    expect(login_page.valid_email()).to_be_visible()
    a=login_page.valid_email()
    print(a.text_content())
    print(a.inner_text())