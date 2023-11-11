import json

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from actions.actions import PageActions
from actions import selectors as sel

class BugBankPageRegistration:
    '''Page class to interact with the BugBank app:'''

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 8)
        self.do = PageActions(self.driver)

    def click_register_btn_to_open_form(self):
        self.do.click(sel.MAIN_REGISTER_BTN)

    def click_back_button(self):
        self.do.click(sel.REG_BACK_BTN)

    def get_back_btn_text(self):
        return self.do.get_text(sel.REG_BACK_BTN)

    def type_email(self, email):
        self.do.type_text(sel.REG_EMAIL_INPUT, email)

    def type_name(self, name):
        self.do.type_text(sel.REG_NAME_INPUT, name)

    def type_password(self, password):
        self.do.type_text(sel.REG_PASSWORD_INPUT, password)

    def type_password_confirmation(self, password):
        self.do.type_text(sel.REG_PW_CONFIRM_INPUT, password)

    def add_balance(self):
        self.do.click(sel.REG_ADD_BALANCE_TOGGLE)

    def click_registration_btn(self):
        self.do.click(sel.REG_REGISTER_BTN)

    def fill_registration_form(self, user_details):
        self.type_email(user_details["email"])
        self.type_name(user_details["name"])
        self.type_password(user_details["password"])
        self.type_password_confirmation(user_details["password"])

    def get_name_input_placeholder_value(self):
        self.do.get_property_value(sel.REG_NAME_INPUT, 'placeholder')

    def get_confirmation_text(self):
        self.wait.until(EC.visibility_of_element_located(sel.MODAL_CONTAINER))
        return self.do.get_text(sel.MODAL_TEXT)

    def get_local_storage_info(self, item):
        self.do.get_local_storage_item(item=item)

    def get_items(self, item):
        local_storage_items = self.do.get_local_storage_items()
        local_storage_user_info_json = local_storage_items[item]
        return json.loads(local_storage_user_info_json)
