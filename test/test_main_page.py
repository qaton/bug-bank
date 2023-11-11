'''Main class that test the BugBank App: TestUrbanRoutes'''
import time

from selenium import webdriver

import pages.login
from fixtures import data
from actions import selectors as sel


class TestBugBankMain:
    '''Main class that test the Urban Routes App functionalities: TestUrbanRoutes'''

    driver = None
    BASE_URL = "https://bugbank.netlify.app/"


    @classmethod
    def setup_class(cls):
        '''
        Método de inicialización de clase. Prepara el driver y la espera implícita de 3 segundos
        '''
        from selenium.webdriver.chrome.service import Service
        service = Service()
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.implicitly_wait(3)
        cls.web_page = pages.login.BugBankPage(cls.driver)
        cls.driver.get(cls.BASE_URL)
        time.sleep(3)

    def test_bugbank_url_should_be_correct(self):
        assert 'https://bugbank.netlify.app/' == self.driver.current_url

    def test_logo_should_be_visible(self):
        logo_src = self.web_page.get_logo_src()
        assert "2Fbugbank" in logo_src

    def test_main_title(self):
        title = self.web_page.get_title()
        assert title == data.MAIN_TITLE

    def test_text_link_to_requirements(self):
        requirements_link_text = self.web_page.get_link_text()
        assert requirements_link_text == data.REQUIREMENTS_LINK_TEXT

    @classmethod
    def teardown_class(cls):
        '''Termina la ejecución del navegador'''
        cls.driver.quit()
