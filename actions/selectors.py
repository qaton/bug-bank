from selenium.webdriver.common.by import By

LOGO_IMG = (By.XPATH, '//*[@id="__next"]/div/div[1]/span/img')
MAIN_TITLE_H1 = (By.XPATH, '//*[@id="__next"]/div/div[1]/h1')
MAIN_DESCRIPTION = (By.XPATH, '//*[@id="__next"]/div/div[1]/p')
MAIN_LINK_REQUEREMENTS = (By.LINK_TEXT, "Conheça nossos requisitos")
MAIN_REGISTER_BTN = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/form/div[3]/button[2]')
MAIN_ACESSAR_BTN = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/form/div[3]/button[1]')

# LOGIN
LOGIN_EMAIL_INPUT = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/form/div[1]/input')
LOGIN_PASSWORD_INPUT = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/form/div[2]/div/input')
LOGIN_EMAIL_LABEL = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/form/div[1]/label')
LOGIN_PASSWORD_LABEL = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/form/div[2]/div/label')
LOGIN_EMAIL_ERROR_TEXT = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/form/div[1]/p')
LOGIN_PASSWORD_ERROR_TEXT = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/form/div[2]/div/p')

# REGISTRATION
REG_BACK_BTN = (By.ID, 'btnBackButton')
REG_EMAIL_INPUT = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/div[2]/input')
REG_NAME_INPUT = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/div[3]/input')
REG_PASSWORD_INPUT = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/div[4]/div/input')
REG_PW_CONFIRM_INPUT = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/div[5]/div/input')
REG_ADD_BALANCE_TOGGLE = (By.ID, 'toggleAddBalance')
REG_REGISTER_BTN = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/button')

# SUCCESS ACCOUNT CREATION MODAL
MODAL_CONTAINER = (By.XPATH, '//*[@id="__next"]/div/div[3]/div')
MODAL_TEXT = (By.ID, 'modalText')
MODAL_CLOSE_BTN = (By.ID, 'btnCloseModal')
MODAL_LINK_CLOSE_X = (By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[1]/a')
