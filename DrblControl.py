from ActionObject import NewItem
from DataFormater import *

chromeDriverPath = 'D:\SOFTWARE\Google\Chrome\Application\chromedriver.exe'


if __name__ == '__main__':
    text = getClipBoardData()
    datas = formatDataByReg(text)

    newItem = NewItem(chromeDriverPath)
    # 登陆

    # userName = input('[系统] 请输入用户名：')
    # password = input('[系统] 请输入密码：')
    # newItem.login(userName, password)
    newItem.login('hophophop', '123456')
    # 跳转至新有好货
    newItem.goToAddNewItemPage()
    # 上传所有内容
    newItem.updateItems(datas)
    # 退出chrome
    newItem.quit()

