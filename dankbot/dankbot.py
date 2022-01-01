from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class DankBot():
    """
    DankBot Class Initialises the Headless browser followed by the necessary automation fucntionalities.
    Controls the curses inlay.
    """
    TYPE_BOX = 'markup-2BOw-j.slateTextArea-1Mkdgw.fontSize16Padding-3Wk7zP'
    BASE_URL = 'https://discord.com'
    DEF_BROWSER = "Chrome"
    driver = ''

    def __init__(self, def_brow='Chrome'):
        self.DEF_BROWSER = def_brow
        if self.DEF_BROWSER == 'Chrome':
            self.driver = webdriver.Chrome()
        elif self.DEF_BROWSER == 'Edge':
            self.driver = webdriver.Edge()
        self.driver.get(self.BASE_URL)
        print("Please Login First")
        print("Also select the channel where you want to the bot to work")

    def exec_base_script(self):
        self.type_box = self.driver.find_element_by_class_name(self.TYPE_BOX)
        self.type_box.send_keys('pls beg')
        self.type_box.send_keys(Keys.ENTER)
        sleep(5)
        self.type_box.send_keys('pls hunt')
        self.type_box.send_keys(Keys.ENTER)
        sleep(5)
        self.type_box.send_keys('pls dig')
        self.type_box.send_keys(Keys.ENTER)
        sleep(5)
        self.type_box.send_keys('pls fish')
        self.type_box.send_keys(Keys.ENTER)
        sleep(5)
        self.type_box.send_keys('pls use horseshoe')
        self.type_box.send_keys(Keys.ENTER)
        sleep(5)    
