'''Main class that test the Urban Routes App functionalities: TestUrbanRoutes'''
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pages.register

class TestUrbanRoutes:
    '''Main class that test the Urban Routes App functionalities: TestUrbanRoutes'''

    driver = None
    BASE_URL="https://bugbank.netlify.app/"


    @classmethod
    def setup_class(cls):
        '''
        Método de inicialización de clase. Prepara el driver y la espera implícita de 3 segundos
        '''
#       from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
        from selenium.webdriver.chrome.service import Service
        service = Service()
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.implicitly_wait(3)

    def test_hello_bugbank(self):

        self.web_page = pages.register.BugBankPage(self.driver)
        self.driver.get(self.BASE_URL)
        assert 'bugbank' in self.driver.current_url


    @classmethod
    def teardown_class(cls):
        '''Termina la ejecución del navegador'''
        cls.driver.quit()
