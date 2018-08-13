from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage
from PageObject.MainPage import MainPage

class LoginPage(BasePage):
    _baseUrl = 'https://drbl.daorc.com/login_login.action'
    _pageTitle = '登录-八斗平台'
    _driver = None

    _userNameInputLoc = (By.CSS_SELECTOR, '#username')
    _passwordInputLoc = (By.CSS_SELECTOR, '#password')
    _loginButtonLoc = (By.CSS_SELECTOR, '#app > section > div.loginBox > form > div:nth-child(4) > div > button')

    def __init__(self, driver):
        self._driver = driver

    def login(self, userName, password):
        self.open()

        self.sendKeys(self._userNameInputLoc, userName)
        self.sendKeys(self._passwordInputLoc, password)
        self.findElement(self._loginButtonLoc).click()

        return MainPage(self._driver)
