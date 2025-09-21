from playwright.sync_api import Page
from test.web.pages.page_base import PageBase

class LoginPage(PageBase):
    def __init__(self, page: Page) -> None:
        super().__init__(page, 
        elements={            
            "username": "#username",
            "password": "#password",
            "login": "#login",
        })

    def login(self, username, password):
        self.element("username").fill(username)
        self.element("password").fill(password)
        self.element("login").click()