from PageObject.BasePage import BasePage
from PageObject.AddNewItemPage import AddNewItemPage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    _baseUrl = 'https://drbl.daorc.com/main_main.action'
    _pageTitle = '八斗会-全部作品 列表界面'
    _driver = None

    _publishNewItemButtonLoc = (By.CSS_SELECTOR, '#li_1001 > a')
    _danPinButtonLoc = (By.CSS_SELECTOR, '#data-trend > div:nth-child(2) > div > div > span > div:nth-child(5)')
    _addNewItemButtonLoc = (By.CSS_SELECTOR, '#danpin > div > div > div:nth-child(1) > a > img')

    def __init__(self, driver):
        self._driver = driver
        #assert self.onPage(self._pageTitle), 'MianPage标题异常'

    def clickPublishNewItemButton(self):
        self.findElement(self._publishNewItemButtonLoc).click()

    def clickDanPinButton(self):
        self.findElement(self._danPinButtonLoc).click()

    def clickAddNewItemButton(self):
        self.findElement(self._addNewItemButtonLoc).click()
        return AddNewItemPage(self._driver)