'''
create on 2018/8/6
@author HoPGoldy

Project: 基础类BasePage，封装所有页面都公用的方法，
定义open函数，重定义find_element，switch_frame，send_keys等函数。
在初始化方法中定义驱动driver，基本url，title
WebDriverWait提供了显式等待方式。

'''

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from selenium.webdriver.support.select import Select


class BasePage:
    _baseUrl = None
    _pageTitle = None
    _driver = None

    # 初始化方法，获取驱动、页面url及标题
    def __init__(self, seleniumDriver,  baseUrl, pageTitle):
        self._driver = seleniumDriver
        self._baseUrl = baseUrl
        self._pageTitle = pageTitle
    
    # 打开页面
    def open(self):
        # print(f'正在打开 {self._baseUrl}')
        self._driver.get(self._baseUrl)
        assert self.onPage(self._pageTitle), '页面标题异常'
        # print('打开完成')

    # 页面是否载入完成
    def onPage(self, pageTitle, delayTime=10):
        # print(f'打开的网页为 {self._driver.title}')
        try:
            WebDriverWait(self._driver, delayTime).until(
                    EC.title_contains(pageTitle)
                )
            return True
        except exceptions.TimeoutException:
            return False
    
    # 查找元素
    def findElement(self, loc, delayTime=10):
        try:
            element = WebDriverWait(self._driver, delayTime).until(
                EC.presence_of_element_located(loc)
            )
            return element
        except exceptions.TimeoutException:
            pass
            # print(f'{self}中未找到{loc}元素')

    # 查找元素集
    def findElements(self, loc, delayTime=10):
        try:
            elements = WebDriverWait(self._driver, delayTime).until(
                EC.presence_of_all_elements_located(loc)
            )
            return elements
        except exceptions.TimeoutException:
            pass
            # print(f'{self}中未找到{loc}元素集')

    # 切换框架
    def switchFrame(self, loc):
        # print(f'将框架切换至{loc}')
        if loc == 'defaultContent':
            return self._driver.switch_to.default_content()
        else:
            return self._driver.switch_to.frame(loc)

    # 页面滚动至元素
    def scrollToElement(self, webElement):
        self.script("arguments[0].scrollIntoView();", webElement)

    # 运行js
    def script(self, src, *arguments):
        return self._driver.execute_script(src, *arguments)

    # 发送数据
    def sendKeys(self, loc, value, clearFirst=True, clickFirst=False):
        WebDriverWait(self._driver, 3).until(
            EC.element_to_be_clickable(loc)
        )
        inputElement = self.findElement(loc)

        if clearFirst:
            inputElement.clear()
        if clickFirst:
            inputElement.click()
        inputElement.send_keys(value)

    # 检查元素是否存在
    def _isElementExisted(self, loc):
        elem = self._driver.find_elements(loc[0], loc[1])
        if len(elem) == 0:
            return False
        else:
            return True

    def setSelectByIndex(self, selectLoc, index):
        element = self.findElement(selectLoc)
        Select(element).select_by_index(index)
