# DrblControl
使用selenium实现的网站drbl.daorc.com的操作封装，本添加了一个剪切板到332类型的数据格式化工具

## 介绍
该脚本可以让你方便快捷的将剪切板的数据上传至该网站

## 安装与配置
### 环境需求
请确保安装可以正常使用的chrome浏览器以及python3.6以上版本

### 安装依赖
cd至根目录下执行以下命令
```pip install -r requirement.txt```

### chrome driver
请查询后在将对应版本的chrome driver放置在你的chrome浏览器根目录下 [驱动下载地址](http://chromedriver.storage.googleapis.com/index.html)，并修改setting.py中的下列属性

```3| CHROME_DRIVER_PATH = '你的chrome驱动路径'```
### 运行脚本
cd至根文件夹下 在命令行中键入

```venv\Scripts\python update.py```

接下来，你应该可以正常的看到程序执行如下操作：

1. 从剪切板读取数据
2. 将数据格式化为指定列表
3. 登陆网站
4. 上传数据
