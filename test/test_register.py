'''Main class that test the Urban Routes App functionalities: TestUrbanRoutes'''

from selenium import webdriver
import json
import pages.register
from fixtures import data
from actions import selectors as sel


class TestBugBankRegister:
    """Main class that test the Urban Routes App functionalities: TestUrbanRoutes"""

    driver = None
    BASE_URL = "https://bugbank.netlify.app/"


    @classmethod
    def setup_class(cls):
        """
        Método de inicialización de clase. Prepara el driver y la espera implícita de 3 segundos
        """
        from selenium.webdriver.chrome.service import Service
        service = Service()
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.implicitly_wait(5)
        # cls.driver.execute_script("window.localStorage.clear();")
        cls.web_page = pages.register.BugBankPageRegistration(cls.driver)
        cls.driver.get(cls.BASE_URL)

    def test_bugbank_url_should_be_correct(self):
        assert 'https://bugbank.netlify.app/' == self.driver.current_url

    def test_transition_to_registration_form(self):
        self.web_page.click_register_btn_to_open_form()
        back_btn_text = self.web_page.get_back_btn_text()
        assert back_btn_text == data.REG_BACK_BTN_TEXT

    def test_valid_user_registration_without_add_balance(self):
        self.web_page.fill_registration_form(user_details=data.VALID_USER)
        self.web_page.click_registration_btn()
        # confirmation_text = self.web_page.get_confirmation_text()
        # assert "foi criada com sucesso" in confirmation_text

    def test_evaluate_local_storage_account(self):
        email = data.VALID_USER["email"]
        local_storage_items = self.web_page.get_items(item=email)

        local_name = local_storage_items["name"]
        local_email = local_storage_items["email"]
        local_password = local_storage_items["password"]
        local_account = local_storage_items["accountNumber"]
        local_balance = local_storage_items["balance"]
        local_is_logged = local_storage_items["logged"]

        assert local_name == data.VALID_USER["name"]
        assert local_email == data.VALID_USER["email"]
        assert local_password == data.VALID_USER["password"]
        assert local_balance == 0

    @classmethod
    def teardown_class(cls):
        """Termina la ejecución del navegador"""
        cls.driver.quit()
