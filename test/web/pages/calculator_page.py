from playwright.sync_api import Page
from test.web.pages.page_base import PageBase

class CalculatorPage(PageBase):
    def __init__(self, page: Page) -> None:
        super().__init__(page, 
        elements={            
            "username": "#user-name", 
            "calculator_screen": "#calculator-screen",

            "key_0": "#key-0",
            "key_1": "#key-1",
            "key_2": "#key-2",
            "key_3": "#key-3",
            "key_4": "#key-4",
            "key_5": "#key-5",
            "key_6": "#key-6",
            "key_7": "#key-7",
            "key_8": "#key-8",
            "key_9": "#key-9",

            "key_add": "#key-add",
            "key_subtract": "#key-subtract",
            "key_multiply": "#key-multiply",
            "key_divide": "#key-divide",

            "key_equals": "#key-equals",
            "key_clear": "#key-clear",

            "toggle_button": "#toggle-button",
            "history": "#history",
            "logout_button": "#logout-button",
        })

    def click_number(self, number):
        self.element(f"key_{number}").click()

    def click_operation(self, operation):
        operation_map = {
            "+": "key_add",
            "-": "key_subtract", 
            "*": "key_multiply",
            "/": "key_divide"
        }
        self.element(operation_map[operation]).click()

    def get_screen_value(self):
        return self.element("calculator_screen").input_value()

    def clear_screen(self):
        self.element("key_clear").click()
    
    def open_history(self):
        self.element("toggle_button").click()

    def logout(self):
        self.element("logout_button").click()