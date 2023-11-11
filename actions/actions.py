from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class PageActions:
    '''
    Class that delivers the main interactions with browsers:
    click, type text, get text, get property values and tab.
    '''

    def __init__(self, driver) -> None:
        self.driver = driver

    def click(self, selector: tuple):
        """
        Perform a click action. Receive a tuple with the selector method
        and the locator.

        Returns: None

        """
        self.driver.find_element(*selector).click()

    def type_text(self, selector: tuple, text: str):
        """
        Types the given text into an element identified by the provided selector.

        Args:
        selector (tuple): A tuple containing the element locator strategy and value.
        text (str): The text to be typed into the element.

        Returns:
        None
        """
        self.driver.find_element(*selector).send_keys(text)

    def get_text(self, selector: tuple) -> str:
        """
        Retrieves the text content of an element identified by the provided selector.

        Args:
            selector (tuple): A tuple containing the element locator strategy and value.

        Returns:
            str: The text content of the element.
        """
        return self.driver.find_element(*selector).text

    def get_property_value(self, selector: tuple, prop: str) -> str:
        """
        Retrieves the specified property value of an element identified by the provided selector.

        Args:
            selector (tuple): A tuple containing the element locator strategy and value.
            prop (str): The name of the property to retrieve.

        Returns:
            str: The value of the specified property.
        """
        return self.driver.find_element(*selector).get_property(prop)

    def press_tab_key(self):
        '''Press the tab key on the web page'''
        ActionChains(self.driver).key_down(Keys.TAB).perform()
