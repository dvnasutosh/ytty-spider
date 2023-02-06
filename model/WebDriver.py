from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

class webDriver:
    def __init__(self,isHeadless:bool=False):
        # Fetching chrome driver Link
        driverLink=webDriver.installWebDriver()
        # Adding Options
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        # activating headless if prompted
        chrome_options.add_argument("--headless") if isHeadless else None
        # Storing the driver instance in instance scoped driver variable
        self.driver= webdriver.Chrome(service=ChromeService(driverLink),options=chrome_options)
        self.driver.implicitly_wait(10)
    
    @staticmethod  
    def installWebDriver():
        """Installs chrome driver automatically

        Returns:
            str: A local to the chrome driver
        """
        return ChromeDriverManager().install()

    def goto(self,link:str)-> None:
        """ fetch data from the url at an instance driver level

        Args:
            link (str):A valid full link of the URL you want to scrap
        """
        self.driver(link)
    
    def getCookies(self,raw:bool=False)->dict|list[dict]:
        """returns the cookie captured from the current website the current instance of webdriver is in

        Args:
            raw (bool, optional): If true will return a name value paired dict else a list of cookies with all it's meta data intact. Defaults to False.

        Returns:
            dict|list[dict]: list of cookies or a cookie name value pair in form of dictionary
        """
        ytcookie=dict()
        if not raw:    
            for i in self.driver.get_cookies():
                ytcookie[i['name']]=i['value']
        else:
            ytcookie=self.driver.get_cookies()
        return ytcookie
    