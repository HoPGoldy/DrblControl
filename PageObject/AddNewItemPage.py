from PageObject.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AddNewItemPage(BasePage):
    _baseUrl = 'https://drbl.daorc.com/data_addData.action?fileTypeId=101&tableFlag=WJ&isopen=0'
    _pageTitle = '八斗会-添加-新有好货'
    _driver = None

    # 自定义分类选择框
    _customCategoryLoc = (By.CSS_SELECTOR, '#CLASSIFYID')
    # 目标人群选择框
    _targetPeople1Loc = (By.CSS_SELECTOR, '#gradeone')
    _targetPeople2Loc = (By.CSS_SELECTOR, '#gradetwo')
    # 亮点选择框以及添加按钮
    _longHighLightAddButtonLoc = (By.CSS_SELECTOR, '#FORTUNATELY_div > div:nth-child(1) > div')
    _longHighLightInput1Loc = (By.CSS_SELECTOR, '#FORTUNATELY_div > div:nth-child(1) > input')
    _longHighLightInput2Loc = (By.CSS_SELECTOR, '#FORTUNATELY_div > div:nth-child(2) > input')
    _longHighLightInput3Loc = (By.CSS_SELECTOR, '#FORTUNATELY_div > div:nth-child(3) > input')
    _shortHighLightInputLoc = (By.CSS_SELECTOR, '#FORTUNATELY_SHORT_text')
    # 加载上次数据对话框选项
    _dismissLoadLastDataAlertLoc = (By.CSS_SELECTOR, '#layui-layer1 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn0')
    _acceptLoadLastDataAlertLoc = (By.CSS_SELECTOR, '#layui-layer1 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn1')

    _getFrameNameDiveLoc = (By.CLASS_NAME, 'layui-layer-iframe')
    # 详情frame
    _openDetailButtonLoc = (By.CSS_SELECTOR, '#COMMODITYLIBRARYID_1_div > img')
    _detailItemTitleInputLoc = (By.CSS_SELECTOR, '#title')
    _itemAddedConfirmLoc = (By.CSS_SELECTOR, '#layui-layer1 > div.layui-layer-btn.layui-layer-btn- > a')
    _itemUrlInputLoc = (By.CSS_SELECTOR, '#url')
    _getItemDetailButtonLoc = (By.CSS_SELECTOR, '#getbutton')
    _saveDetailButtonLoc = (By.CSS_SELECTOR, '#toNextbutton')
    # 补充内容frame
    _openAdditionButtonLoc = (By.CLASS_NAME, 'COVERIMG')
    _additionTitleInputLoc = (By.CSS_SELECTOR, '#title')
    _additionBrandInputLoc = (By.CSS_SELECTOR, '#bname')
    _additionContentInputLoc = (By.CSS_SELECTOR, '#describe')
    _saveAdditionButtonLoc = (By.CSS_SELECTOR, '#dataform > div > div:nth-child(1) > div > div.btn-group.btn-group-justified > a')
    _addNewAdditionButtonLoc = (By.CSS_SELECTOR, '#addTable > tbody > tr:nth-child(10) > td.inputValue.showTd > div.btn-group.btn-group-justified > a.btn.btn-success')
    # 保存草稿
    _saveDraftButtonLoc = (By.CSS_SELECTOR, '#saveTempDataButton')
    _addNextItemButtonLoc = (By.CSS_SELECTOR, '#layui-layer1 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn1')
    _goToListButtonLoc = (By.CSS_SELECTOR, '#layui-layer1 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn2')
    
    def __init__(self, driver):
        self._driver = driver

    # 设置自定义分类
    def setCustomCategoryByIndex(self, index):
        self.setSelectByIndex(self._customCategoryLoc, index)

    # 设置目标人群
    def setTragetPeopleByIndex(self, targetTypeIndex, peopleTypeIndex):
        self.setSelectByIndex(self._targetPeople1Loc, targetTypeIndex)
        self.setSelectByIndex(self._targetPeople2Loc, peopleTypeIndex)

    # 添加长亮点
    def addLongHighLightNum(self, highLightNum):
        longHighLightAddButton = self.findElement(self._longHighLightAddButtonLoc)
        self.scrollToElement(longHighLightAddButton)
        for i in range(0, highLightNum):
            longHighLightAddButton.click()

    # 输入长亮点
    def inputLongHighLight(self, value, highLightCode=0):
        firstLongHighLightInput = self.findElement(self._longHighLightInput1Loc)
        # self.scrollToElement(firstLongHighLightInput)

        if highLightCode == 1:
            self.sendKeys(self._longHighLightInput2Loc, value)
        elif highLightCode == 2:
            self.sendKeys(self._longHighLightInput3Loc, value)
        else:
            self.sendKeys(self._longHighLightInput1Loc, value)

    # 输入短亮点
    def inputShortHighLight(self, value):
        shortHighLightInput = self.findElement(self._shortHighLightInputLoc)
        self.scrollToElement(shortHighLightInput)

        self.sendKeys(self._shortHighLightInputLoc, value)
        self.sendKeys(self._shortHighLightInputLoc, Keys.ENTER, clearFirst=False)
        
    # 处理刚进入网页时的“载入上次数据”对话框
    def dealLoadLastDataAlert(self, confirm=False):
        print('[新有好货] 检查是否出现载入数据弹窗')
        dismissButton = self.findElement(self._dismissLoadLastDataAlertLoc, 3)
        if dismissButton:
            if confirm:
                self.findElement(self._acceptLoadLastDataAlertLoc).click()
            else:
                dismissButton.click()
            print('[新有好货] 弹窗已处理')
            return
        print('[新有好货] 未出现弹窗')

    # 打开详情frame
    def openDetailFrame(self, itemUrl):
        self.findElement(self._openDetailButtonLoc).click()
        frameName = self._getFrameNameByDiv(self._getFrameNameDiveLoc)
        self.switchFrame(frameName)
        self.sendKeys(self._itemUrlInputLoc, itemUrl)
        self.findElement(self._getItemDetailButtonLoc).click()

    # 处理商品已重复添加对话框
    def dealItemAddedAlert(self):
        itemAddedConfirmButton = self.findElement(self._dismissLoadLastDataAlertLoc, 3)
        if itemAddedConfirmButton:
            itemAddedConfirmButton.click()

    # 保存并关闭详情frame
    def saveDetailFrame(self):
        self.findElement(self._saveDetailButtonLoc).click()
        self.switchFrame('defaultContent')

    # 填写详情frame中的商品名称
    def inputTitleInFrame(self, itemTitle):
        self.sendKeys(self._detailItemTitleInputLoc, itemTitle)

    # 根据存放frame的div获取frame的名称
    def _getFrameNameByDiv(self, loc):
        return self.findElement(loc).get_attribute('id').replace('layer', 'layer-iframe')

    # 打开补充frame
    def openAdditionFrame(self, additionCode=0):
        openImgs = self.findElements(self._openAdditionButtonLoc)
        openImgs[additionCode + 1].click()
        frameName = self._getFrameNameByDiv(self._getFrameNameDiveLoc)
        self.switchFrame(frameName)

    # 保存并关闭补充frame
    def saveAdditionFrame(self):
        self.findElement(self._saveAdditionButtonLoc).click()
        self.switchFrame('defaultContent')

    # 添加新的自定义段落
    def addNewCustomAddition(self):
        addNewAdditionButton = self.findElement(self._addNewAdditionButtonLoc)
        self.scrollToElement(addNewAdditionButton)
        addNewAdditionButton.click()

    # 填写补充名
    def inputAdditionTitle(self, title):
        self.sendKeys(self._additionTitleInputLoc, title)
    
    # 填写品牌名称
    def inputAdditionBrand(self, brand):
        self.sendKeys(self._additionBrandInputLoc, brand)

    # 填写补充内容
    def inputAdditionContent(self, content):
        self.sendKeys(self._additionContentInputLoc, content)
    
    # 保存条目
    def saveItem(self):
        self.findElement(self._saveDraftButtonLoc).click()

    # 添加新内容
    def addNextItem(self):
        self.findElement(self._addNextItemButtonLoc).click()

    # 前往内容列表
    def goToList(self):
        self.findElement(self._goToListButtonLoc).click()