from ActionObject import NewItem
from DataFormater import *
import setting


def update(datas):
    print('[系统] 开始上传')
    newItem = NewItem(setting.CHROME_DRIVER_PATH)

    # 登陆
    userName = input('[系统] 请输入用户名：')
    password = input('[系统] 请输入密码：')
    newItem.login(userName, password)

    # 跳转至新有好货
    newItem.goToAddNewItemPage()
    # 上传所有内容
    newItem.updateItems(datas)
    # 退出chrome
    newItem.quit()


if __name__ == '__main__':
    input('[系统] 请复制资源后回车')
    text = getClipBoardData()
    print('[系统] 正在整理资源')
    datas = formatDataByReg(text)
    comm = input('[系统] 整理完成 1-检查作业 回车-开始上传：')

    if comm != '1':
        update(datas)
    else:
        show(datas)
        comm = input('[系统] 1-退出 回车-开始上传')
        if comm != '1':
            update(datas)

