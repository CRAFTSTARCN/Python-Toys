#python
import requests
from bs4 import BeautifulSoup
import urllib
import time
import random

fileSpan = random.choice([True,False])
ask = input("是否生成文件？[y/n]")
if ask == "y":
    fileSpan = True
if ask == "n":
    fileSpan = False


link = "https://www.bilibili.com/ranking?"

page = requests.get(link).content.decode("utf-8")
soup = BeautifulSoup(page,'lxml')

urllist = soup.select(".info a")

if fileSpan :
    todayFile = open("./outHTML/"+time.strftime("%Y.%m.%d")+".html", "wt+",encoding='utf-8')
    todayFile.write("<!DOCTYPE html>\n<html>\n<head>\n<meta charset = \"utf-8\">\n<h1>今日BILIBIL榜单</h1>\n</head>\n<body>\n<div>\n")

j = 1
for i in range(0,urllist.__len__(),2):
    uplordurl = "http:"+urllist[i+1]['href']
    uplordPage = requests.get(uplordurl).content.decode("utf-8")
    upSoup = BeautifulSoup(uplordPage,'lxml')
    upTitleL = upSoup.select("title")
    afterPro = str(upTitleL[0]).split('-')
    orderTitle = "第"+str(j)+"名："
    vedioName = urllist[i].text
    vedioLink = "视频链接url："+ str(urllist[i]['href'])
    uplordInfo = "UP主：" + afterPro[0][7:-6] + '\n' + "UP主的主页：" + uplordurl
    print(orderTitle,'\n',vedioName,'\n',vedioLink,'\n',uplordInfo)
    if fileSpan:
        todayFile.write("<li>"+orderTitle+"</li>\n")
        todayFile.write("<ul style=\"list-style: circle;\">\n")
        todayFile.write("<li><a href = \""+str(urllist[i]['href'])+"\">"+vedioName+"</a></li>\n")
        todayFile.write("<li><a href = \""+uplordurl+"\">UP主："+afterPro[0][7:-6]+"</a></li>\n</ul>\n")
    j = j+1


if fileSpan:
    todayFile.write("</div>\n</body>\n</html>")
    todayFile.close()
