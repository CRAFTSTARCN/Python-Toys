#爬虫
print("获取最新数据")
if __name__ == "__main__":
    print("这是网络爬虫模块，请从main.py启动")
    quit()

import requests
from bs4 import BeautifulSoup
import urllib

infoLink = "https://3g.dxy.cn/newh5/view/pneumonia?"
infoPage = requests.get(infoLink).content.decode('utf-8')
infoSoup = BeautifulSoup(infoPage, 'lxml')
infoList = infoSoup.select('#getStatisticsService')
infoStr  = infoList[0].text
def findData(a:str)->str():
    tagPosition = infoStr.find(a)
    mapPosition = infoStr.find(':',tagPosition)
    endPistionn = infoStr.find(',',mapPosition)
    return infoStr[mapPosition+1 : endPistionn]

