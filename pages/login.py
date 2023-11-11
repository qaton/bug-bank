from selenium.webdriver.support.wait import WebDriverWait

from actions.actions import PageActions
from actions import selectors as sel


class BugBankPage:
    """Page class to interact with the BugBank app"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.do = PageActions(self.driver)

    def get_logo_src(self):
        return self.do.get_property_value(sel.LOGO_IMG, "src")

    def get_title(self):
        return self.do.get_text(sel.MAIN_TITLE_H1)

    def get_link_text(self):
        return self.do.get_text(sel.MAIN_LINK_REQUEREMENTS)
