# DrblControl
使用selenium实现的网站drbl.daorc.com的操作封装

## 介绍
该控制器采用了selenium的PO模型，将drbl.daorc.com的主要操作封装起来方便调用，主要包含以下操作：

1. **登陆**
2. **跳转至新建好货**
3. **填充内容**
4. **保存条目**
4. 更详细的操作请参见PageObject文件夹中的文件

## 安装与配置
### 环境需求
请确保安装python3.6.2以上的版本和可以正常使用的chrome浏览器
### 安装依赖
```pip3 install -r requirements.txt```
### chrome驱动
请将对应版本的chrome驱动放置在你的chrome浏览器根目录下，并修改ActionObject.py中的下列属性

```3| chromeDriverPath = '你的chrome驱动路径'```
### 运行测试用例
cd至根文件夹下 在命令行中键入

```python DrblControl.py```

接下来，你应该可以正常的通过DrblControl.py中提供的例子

## 功能说明
以下将说明定义在**ActionObject.py**中**NewItem**类的所有功能

### login(userName, password)
接受用户名和密码，登陆网站，暂未实现登陆失败的提示功能

### goToAddNewItemPage()
不接受参数，将页面跳转至单品的新有好货页面

### updateItems(datas)
接受一个包含数据的元组，并将其依次上传至网站

### fillData(data)
接受一个包含单个条目的字典，并将其上传至网站，data的结构请参考下一小节

### saveItem(operation)
接受一个字符串类型的操作名，并在保存草稿后按规定的操作执行，支持的操作如下(不支持的操作将触发默认动作)

1. **goToList**：返回列表（默认）
2. **addNewItem**: 新建下一条

## 传入的data字典结构
你也可以在DrblControl.py中找到下列说明
```
    {
    'category': 9, #自定义分类的索引值
    'targetPeople': (10, 1),#目标人群的索引值
    'url': 'https://detail.tmall.com/item.htm?id=574974684040',#商品链接
    'title': '品牌 商品名',#商品名
    'longHighLight': ('长亮点', '长亮点2', '长亮点3'),#长亮点，不规定数量，但八斗会最多支持三个，传入过数量过多的长亮点将导致异常
    'shortHighLight': ('短亮点1', '短亮点2', '短亮点3'),#短亮点，要求同长亮点
    'addition': ({#补充内容，为元组类型，支持传入多个补充
        'title': '设计亮点',#补充标题
        'content': '设计亮点的内容。'},#补充内容
                {
        'title': '品牌介绍',#补充2标题
        'content': '品牌介绍的内容。',#补充2内容
        'brand': 'brand'#该属性将将被添加至补充的品牌名输入框中，需先确保title值为'品牌介绍'，不然将导致异常
            },
        ...)
    }
```

## 项目结构
  ### PageObject/BaseObject.py
  该文件二次封装了selenium提供的接口以便于项目使用

  ### PageObject/其余python文件
  包括 **LoginPage.py**，**AddNewItemPage.py**，**MainPage.py**

  这三个文件提供了主要的动作方法以及页面元素的定位器

  ### ActionObject.py
  该文件使用了LoginPage.py，AddNewItemPage.py，MainPage.py中提供的动作方法并组装成上文**介绍**中说明的具体功能

  ### DrblControl.py
  该文件提供了一组测试数据以及一个具体的actionObject调用例子，该例子将访问你的账户并上传两条包含测试数据的条目
