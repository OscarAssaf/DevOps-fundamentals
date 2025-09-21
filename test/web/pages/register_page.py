from playwright.sync_api import Page
from test.web.pages.page_base import PageBase

class RegisterPage(PageBase):
    def __init__(self, page: Page) -> None:
        super().__init__(page, 
        elements={            
            "register": "#register",
            "username": "#username",
            "password1": "#password1",
            "password2": "#password2",
            "register": "#register",
        })

    def register(self, username, password):
        self.element("register").click()
        self.element("username").fill(username)
        self.element("password1").fill(password)
        self.element("password2").fill(password)
        self.element("register").click()