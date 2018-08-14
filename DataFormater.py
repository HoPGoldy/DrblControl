# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 16:39
# @Author  : HoPGoldy

import win32clipboard as w
import win32con
import re
import random

dataSplitReg = r'━━━━第[0-9]+个条目━━━━[\s]+'
urlReg = '[\S]+(?=\r\n)'
brandReg = r'(?<=宝贝名：\r\n)[\S]+'
titleReg = r'(?<=[\s])[\S]+(?=\r\n长亮点)'
longHighLightsReg = r'(?<=长亮点：\r\n)[\S]+\r\n[\S]+\r\n[\S]+'
shortHighLightReg = r'(?<=短亮点：\r\n)[\S]+\r\n[\S]+\r\n[\S]+'
designHighlightReg = r'(?<=设计亮点\r\n)[\S]+'


def getClipBoardData():
    w.OpenClipboard()
    text = w.GetClipboardData(win32con.CF_UNICODETEXT)
    w.CloseClipboard()

    return text


def formatDataByCode(text):
    temps = text.split('^^^')
    datas = []
    for data in temps:
        dataTemps = data.split('|||')
        data = {
            'category': 9,
            'targetPeople': (10, random.randint(1, 5)),
            'url': dataTemps[0],
            'title': dataTemps[1],
            'longHighLight': ('长亮点1长亮点1，长亮点1。', '长亮点2长亮点2，长亮点2。', '长亮点3长亮点3，长亮点3。'),
            'shortHighLight': ('短亮点1短亮点1', '短亮点2短亮点2', '短亮点3短亮点3'),
            'addition': ({
                'title': '设计亮点',
                'content': '设计亮点设计亮点设计亮点设计亮点设计亮点设计亮点设计亮点设计亮点设计亮点设计亮点设计亮点设计亮点设计亮点设计亮点设计亮点设计亮点。'},
                         {
                'title': '品牌介绍',
                'content': '品牌介绍品牌介绍品牌介绍品牌介绍品牌介绍品牌介绍品牌介绍品牌介绍品牌介绍品牌介绍品牌介绍品牌介绍品牌介绍品牌介绍品牌介绍品牌介绍。',
                'brand': 'brand'})
            }
        for i in range(0, len(dataTemps)):
            print(dataTemps[i])


def formatDataByReg(text):
    dataTemps = re.split(dataSplitReg, text)
    datas = []
    for i in range(1, len(dataTemps)):
        dataTemp = dataTemps[i]
        data = {
            'category': 9,
            'targetPeople': (10, 1),
            'url': getUrl(dataTemp),
            'title': f'{getBrand(dataTemp)} {getTitle(dataTemp)}',
            'longHighLight': getLongHighLights(dataTemp),
            'shortHighLight': getShortHighLights(dataTemp),
            'addition': ({
                             'title': '设计亮点',
                             'content': getDesignHighlight(dataTemp)},
                         {
                             'title': '品牌介绍',
                             'content': '                                                             ',
                             'brand': getBrand(dataTemp)})
            }
        datas.append(data)
    return datas


def getUrl(data):
    return re.search(urlReg, data).group(0)


def getBrand(data):
    return re.search(brandReg, data).group(0)


def getTitle(data):
    return re.search(titleReg, data).group(0)


def getLongHighLights(data):
    longHighLightsText = re.search(longHighLightsReg, data).group(0)
    return re.split(r'\r\n', longHighLightsText)


def getShortHighLights(data):
    shortHighLightsText = re.search(shortHighLightReg, data).group(0)
    return re.split(r'\r\n', shortHighLightsText)


def getDesignHighlight(data):
    return re.search(designHighlightReg, data).group(0)