#python

import requests
from bs4 import BeautifulSoup
import urllib
import random

want  = int(input("Enter the pages you wanna grab:"))
pages = 1

wantFile = random.choice([True,False])
fileKey  = input("Wanna span a file?[y/n]")
if fileKey == 'y':
    wantFile = True
if fileKey == 'n':
    wantFile = False

if wantFile:
    discountFile = open("./outHTML/Steam_Discont.txt", "wt+", encoding="utf-8")

while True:
    if pages > want:
        break
    disconturl  = "https://store.steampowered.com/search/?specials=1&page="+str(pages)
    discontPage = requests.get(disconturl).content.decode('utf-8')
    discontSoup = BeautifulSoup(discontPage,'lxml')

    nameList      = discontSoup.select(".search_name .title")
    if nameList.__len__() == 0:
        break
    releasLsit    = discontSoup.select(".search_released")
    discountList  = discontSoup.select(".search_discount")
    discountPrice = discontSoup.select(".search_price")

    for i in range(0,nameList.__len__()):
        print("游戏名：",nameList[i].text,"发行日期：",releasLsit[i].text,"折扣力度：",discountList[i].text.replace("\n",""),"原价/现价：",str(discountPrice[i].text).replace("\n",""))
        if wantFile :
            discountFile.write("游戏名："+nameList[i].text+"发行日期："+releasLsit[i].text+"折扣力度："+discountList[i].text.replace("\n","")+"原价/现价："+str(discountPrice[i].text).replace("\n","")+'\n')
    pages = pages+1

if wantFile:
    discountFile.close()
