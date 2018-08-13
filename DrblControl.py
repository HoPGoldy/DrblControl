from ActionObject import NewItem

chromeDriverPath = 'D:\SOFTWARE\Google\Chrome\Application\chromedriver.exe'

data = {
    'category': 9,
    'targetPeople': (10, 1),
    'url': 'https://detail.tmall.com/item.htm?id=574974684040',
    'title': '品牌 商品名',
    'longHighLight': ('长亮点1长亮点1，长亮点1。', '长亮点2长亮点2，长亮点2。', '长亮点3长亮点3，长亮点3。'),
    'shortHighLight': ('短亮点1短亮点1', '短亮点2短亮点2', '短亮点3短亮点3'),
    'addition': ({
        'title': '设计亮点',
        'content': '设计亮点设计亮点设计亮点设计亮点设计亮点设计亮点设计亮点设计亮点设计亮点设计亮点设计亮点设计亮点设计亮点设计亮点设计亮点设计亮点。'},
                {
        'title': '品牌介绍',
        'content': '品牌介绍品牌介绍品牌介绍品牌介绍品牌介绍品牌介绍品牌介绍品牌介绍品牌介绍品牌介绍品牌介绍品牌介绍品牌介绍品牌介绍品牌介绍品牌介绍。',
        'brand': 'brand'
            })
    }

if __name__ == '__main__':
    newItem = NewItem(chromeDriverPath)
    #登陆
    userName = input('[系统] 请输入用户名：')
    password = input('[系统] 请输入密码：')
    newItem.login(userName, password)
    #跳转至新有好货
    newItem.goToAddNewItemPage()
    #上传所有内容
    newItem.updateItems((data, data))
    #退出chrome
    newItem.quit()
    