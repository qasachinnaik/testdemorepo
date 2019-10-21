import sys, os; sys.path.insert(0, os.path.abspath('..'));
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pytest
from pages.page import Page


class HomePage(Page):

    _url = '{base_url}'

    _home_text_locator = (By.CSS_SELECTOR, "#menu-item-2002 a")
    _portfolio_text_locator = (By.ID, "menu-item-2001")
    _view_work = (By.CSS_SELECTOR, "div.slider-content .slider-txt.slider-txt-btn")
    _scroll_top_page = (By.ID, "wpfront-scroll-top-container")
    _services_dropdown = (By.CSS_SELECTOR, "a.dropdown-toggle .caret")
    _qaassurance_services_option = (By.CSS_SELECTOR, "#menu-item-4096")
    _contact_us = (By.CSS_SELECTOR, "#menu-item-2000 a")

   
    

    @property
    def verify_home_page(self):
        return self.selenium.find_element(*self._home_text_locator).text

    def portfolio_page_route(self):
    	self.selenium.find_element(*self._portfolio_text_locator).click()
    	

    def view_our_work(self):
    	self.selenium.find_element(*self._view_work).click()

    def scroll_top(self):
    	self.selenium.find_element(*self._scroll_top_page).click()

    def scroll_down(self):
        self.selenium.execute_script("window.scrollTo(0, 1080)")
        time.sleep(10)

    def services_dropdown(self):
        self.selenium.find_element(*self._services_dropdown).click()

    def qaassurance_dropdown(self):
        self.selenium.find_element(*self._qaassurance_services_option).click()

    def contact_us(self):
        self.selenium.find_element(*self._contact_us).click()

    # def window_zero(self):
    #     window_before = self.selenium.window_handles[0]


    # def window_one(self):
    #     window_after = self.selenium.window_handles[1]

    # def window_switch(self):
    #     wz = self.window_zero()
    #     self.selenium.switch_to.window(wz)


    
    def switch_tab_one(self,driver):
        return self.selenium.window_handles[0] 
        

    
    def switch_tab_two(self,driver):
        self.selenium.window_handles[1]
        return driver.switch_to.window(self.switch_tab_one(driver))
        


    	
