
import sys, os; sys.path.insert(0, os.path.abspath('..'));
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
from pages.home import HomePage
#from dashboard import DashboardPage




def test_invalid_login(base_url_live, driver):
    """Attempt to log in with an invalid username and password"""

    home_page = HomePage(base_url_live, driver).open()
    assert "HOME"  in home_page.verify_home_page 
    assert  "Home" in driver.title
   
def test_view_our_work_button(base_url_live, driver):
	home_page = HomePage(base_url_live, driver).open()
	home_page.switch_tab_one(driver)
	home_page.view_our_work()
	home_page.switch_tab_two(driver)
	

def test_portfolio(base_url_live, driver):
	home_page = HomePage(base_url_live, driver).open()
	home_page.portfolio_page_route()

def test_scroll_down(base_url_live, driver):
	home_page = HomePage(base_url_live, driver).open()
	home_page.scroll_down()
	home_page.scroll_top()

def test_services_dropdown(base_url_live, driver):
	home_page = HomePage(base_url_live, driver).open()
	home_page.services_dropdown()
	home_page.qaassurance_dropdown()

def test_contact_us(base_url_live, driver):
	home_page = HomePage(base_url_live, driver).open()
	home_page.contact_us()

