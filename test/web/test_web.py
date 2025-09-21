from test.web.test_base import WebBase
from test.web.pages.login_page import LoginPage
from test.web.pages.register_page import RegisterPage
from test.web.pages.calculator_page import CalculatorPage
from playwright.sync_api import expect
import pytest

class TestWeb(WebBase):
    def test_login(self):
        LoginPage(self.page).login(username="admin", password="test1234")
        expect(CalculatorPage(self.page).element("username")).to_have_text("admin")

    def test_register_new_user(self):
        CalculatorPage(self.page).logout()
        register_page = RegisterPage(self.page)
        register_page.register(username="hello12345", password="hi212")
        expect(CalculatorPage(self.page).element("username")).to_have_text("hello12345")

    
    def test_calculator_add(self):
        calc_page = CalculatorPage(self.page)
        calc_page.clear_screen()
        
        #5 + 3 = 8
        calc_page.click_number(5)
        calc_page.click_operation("+")
        calc_page.click_number(3)
        calc_page.element("key_equals").click()
        
        # verify
        expect(calc_page.element("calculator_screen")).to_have_value("8")

    def test_calculator_subtract(self):
        calc_page = CalculatorPage(self.page)
        calc_page.clear_screen()
        
        #9 - 4 = 5
        calc_page.click_number(9)
        calc_page.click_operation("-")
        calc_page.click_number(4)
        calc_page.element("key_equals").click()
        
        #verify
        expect(calc_page.element("calculator_screen")).to_have_value("5")

    def test_calculator_multiply(self):
        calc_page = CalculatorPage(self.page)
        calc_page.clear_screen()
        
        #6 * 7 = 42
        calc_page.click_number(6)
        calc_page.click_operation("*")
        calc_page.click_number(7)
        calc_page.element("key_equals").click()
        
        # asser
        expect(calc_page.element("calculator_screen")).to_have_value("42")

    def test_calculator_divide(self):
        calc_page = CalculatorPage(self.page)
        calc_page.clear_screen()
        
        # 8/2 =4
        calc_page.click_number(8)
        calc_page.click_operation("/")
        calc_page.click_number(2)
        calc_page.element("key_equals").click()
        
        # asser
        expect(calc_page.element("calculator_screen")).to_have_value("4")


    def test_history_feature(self):
         
        CalculatorPage(self.page).logout()
        #login
        login_page = LoginPage(self.page)
        login_page.login(username="admin", password="test1234")
        
        #initiate calc
        calc_page = CalculatorPage(self.page)
        
        # calc 1
        calc_page.click_number(3)
        calc_page.click_operation("+")
        calc_page.click_number(3)
        calc_page.element("key_equals").click()
        
        #calc 2
        calc_page.click_number(5)
        calc_page.click_operation("-")
        calc_page.click_number(2)
        calc_page.element("key_equals").click()
        
        #history
        calc_page.open_history()
        #assert
        expect(calc_page.element("history")).to_have_value("3+3=6\n5-2=3\n")