#爬虫
print("获取最新数据")
if __name__ == "__main__":
    print("这是网络爬虫模块，请从main.py启动")
    quit()

import requests
from bs4 import BeautifulSoup
import urllib
import json

#获取全国信息
infoLink = "https://3g.dxy.cn/newh5/view/pneumonia?"
infoPage = requests.get(infoLink).content.decode('utf-8')
infoSoup = BeautifulSoup(infoPage, 'lxml')
infoList = infoSoup.select('#getStatisticsService')
infoStr  = infoList[0].text
def findData(a:str)->str:
    tagPosition = infoStr.find(a)
    mapPosition = infoStr.find(':',tagPosition)
    endPistionn = infoStr.find(',',mapPosition)
    return infoStr[mapPosition+1 : endPistionn]


#获取Json
provJsonTag   = infoSoup.select("#getAreaStat")[0].text
provJsonStart = provJsonTag.find("[")
provJsonEnd   = provJsonTag.rfind("]")
provJsonStr   = provJsonTag[provJsonStart:provJsonEnd+1]


#写入Json
with open("data.json",'w', encoding='utf-8') as jsFile:
    jsFile.write(provJsonStr)

#读取Json
with open("data.json",'r', encoding='utf-8') as jsFile:
    jsObj = json.load(jsFile)

provNames   = list()
provNumber  = list()

for maps in jsObj :
    provNames.append(maps['provinceShortName'])
    provNumber.append(maps['confirmedCount'])

for na,nu in zip(provNames,provNumber) :
    print(na,":",nu)