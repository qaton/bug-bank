from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from actions import selectors as sel
from actions.actions import PageActions


class BugBankPage:
    '''Page class to interact with the BugBank app:'''

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)
        self.action = PageActions(self.driver)


    def click_register_btn(self):
        self.action.click(*sel.REGISTER_BTN)
