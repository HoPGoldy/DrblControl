# DrblControl
使用selenium实现的网站drbl.daorc.com的操作封装，本添加了一个剪切板到332类型的数据格式化工具

## 介绍
该脚本可以让你方便快捷的将剪切板的数据上传至该网站

## 安装与配置
### 环境需求
请确保安装python3.6.2以上的版本和可以正常使用的chrome浏览器

### chrome驱动
请将对应版本的chrome驱动放置在你的chrome浏览器根目录下，并修改ActionObject.py中的下列属性

```3| chromeDriverPath = '你的chrome驱动路径'```
### 运行脚本
cd至根文件夹下 在命令行中键入

```venv\Scripts\python DrblControl.py```

接下来，你应该可以正常的看到程序执行如下操作：

1. 从剪切板读取数据
2. 将数据格式化为指定列表
3. 登陆网站
4. 开始上传
