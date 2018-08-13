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

## 项目结构
