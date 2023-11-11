from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

import fixtures.selectors as sel
from utils.interceptor import intercept_response
from utils.code_retriever import retrieve_phone_code

class UrbanRoutesPage:
    '''Page class to interact with the Urban Routes app: UrbanRoutesPage(driver)'''
    CODE = None

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 40)

    def press_tab_key(self):
        '''Press the tab key on the web page'''
        ActionChains(self.driver).key_down(Keys.TAB).perform()

    def set_from(self, from_address):
        '''Set the address from where the user is. set_from(addres: string)'''
        self.driver.find_element(*sel.from_field).send_keys(from_address)

    def set_to(self, to_address):
        '''Set the destination address. set_to(addres: string)'''
        self.driver.find_element(*sel.to_field).send_keys(to_address)

    def get_from(self):
        '''Return the "from" address as a string'''
        return self.driver.find_element(*sel.from_field).get_property('value')

    def get_to(self):
        '''Return the "to" address as a string'''
        return self.driver.find_element(*sel.to_field).get_property('value')
