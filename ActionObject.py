from PageObject.LoginPage import LoginPage
from selenium import webdriver
from selenium.common import exceptions


class NewItem:
    _driver = None

    _loginPage = None
    _mainPage = None
    _addNewItemPage = None

    # 启动chrome
    def __init__(self, chromeDriverPath):
        print('[系统] 正在启动chrome')
        startOption = webdriver.ChromeOptions()
        # startOption.set_headless()
        try:
            driver = webdriver.Chrome(chromeDriverPath, options=startOption)
            driver.set_window_size(1280, 2000)
            self._driver = driver
            print('[系统] 启动成功')
        except exceptions.WebDriverException:
            print('[系统] 启动失败')

    # 登陆八斗会
    def login(self, userName, password):
        loginPage = LoginPage(self._driver)
        
        mainPage = loginPage.login(userName, password)
        print('[系统] 登陆完成')
        self._loginPage = loginPage
        self._mainPage = mainPage

    # 跳转至新建好货页面
    def goToAddNewItemPage(self):
        mainPage = self._mainPage

        print('[系统] 正在跳转至新建好货页面')
        mainPage.clickPublishNewItemButton()
        mainPage.clickDanPinButton()
        addNewItemPage = mainPage.clickAddNewItemButton()
        print('[系统] 跳转完成')
        addNewItemPage.dealLoadLastDataAlert()

        self._mainPage = mainPage
        self._addNewItemPage = addNewItemPage

    # 上传多个条目
    def updateItems(self, datas):
        for i in range(0, len(datas)):
            print(f'\n[系统] 正在上传第{i+1}条')
            item = datas[i]
            self.fillData(item)
            if i != (len(datas)-1):
                self.saveItem('addNewItem')
            else:
                self.saveItem('goToList')

    # 上传单个条目
    def fillData(self, data):
        addNewItemPage = self._addNewItemPage
        # 填写自定义分类及目标人群
        print('[上传内容] 选择自定义分类')
        addNewItemPage.setCustomCategoryByIndex(data['category'])

        # 填写url及详情内的商品名
        print('[上传内容] 填写url及名称')
        addNewItemPage.openDetailFrame(data['url'])
        addNewItemPage.dealItemAddedAlert()
        addNewItemPage.inputTitleInFrame(data['title'])
        addNewItemPage.saveDetailFrame()

        # 填写长亮点短亮点
        print('[上传内容] 填写长亮点')
        longHighLightNum = len(data['longHighLight'])
        addNewItemPage.addLongHighLightNum(longHighLightNum - 1)
        for i in range(0, longHighLightNum):
            addNewItemPage.inputLongHighLight(data['longHighLight'][i], i)
        print('[上传内容] 填写短亮点')
        for i in range(0, len(data['shortHighLight'])):
            addNewItemPage.inputShortHighLight(data['shortHighLight'][i])
    
        # 填写补充
        additionNum = len(data['addition'])
        for i in range(0, additionNum):
            print(f'[上传内容] 填写第{i+1}个补充内容')
            addNewItemPage.openAdditionFrame(i)
            
            addNewItemPage.inputAdditionTitle(data['addition'][i]['title'])
            addNewItemPage.inputAdditionContent(data['addition'][i]['content'])
            if 'brand' in data['addition'][i]:
                addNewItemPage.inputAdditionBrand(data['addition'][i]['brand'])

            addNewItemPage.saveAdditionFrame()
            if i != (additionNum-1):
                addNewItemPage.addNewCustomAddition()

        print('[上传内容] 选择目标人群')
        addNewItemPage.setTragetPeopleByIndex(data['targetPeople'][0], data['targetPeople'][1])

        self._addNewItemPage = addNewItemPage

    # 保存并添加新条目或返回列表
    def saveItem(self, operation='goToList'):
        addNewItemPage = self._addNewItemPage

        addNewItemPage.saveItem()
        if operation == 'goToList':
            print('[保存] 返回列表')
            addNewItemPage.goToList()
        elif operation == 'addNewItem':
            print('[保存] 新建下一条')
            addNewItemPage.addNextItem()
        else:
            print('[保存] 返回列表')
            addNewItemPage.goToList()

        self._addNewItemPage = addNewItemPage

    def quit(self):
        print('\n[系统] 正在关闭chrome')
        self._driver.quit()
        print('[系统] 关闭完成')
