import matplotlib.pyplot as plt 
import numpy as npy 
import fileReader
import time

#时间对照表
monthTransfer = {1:"一",2:"二",3:"三",4:"四",5:"五",6:"六",7:"七",8:"八",9:"九",10:"十",11:"十一",12:"十二"}


#爬虫
import requests
from bs4 import BeautifulSoup
import urllib

infoLink = "https://3g.dxy.cn/newh5/view/pneumonia?"
infoPage = requests.get(infoLink).content.decode('utf-8')
infoSoup = BeautifulSoup(infoPage, 'lxml')
infoList = infoSoup.select('.content___2hIPS span')

print("确诊：",infoList[0].text," 疑似：",infoList[1].text," 治愈：",infoList[2].text," 死亡：",infoList[3].text)


#预处理，检测是否已经过了一天
if fileReader.diff_int == 0 :
    fileReader.numberList[-1] = int(infoList[0].text)
else:
    fileReader.dateList.append(fileReader.dateList[-1]+fileReader.diff_int)
    month = int(time.strftime("%m"))
    Latestdate = monthTransfer[month]+"月"+time.strftime("%d")
    fileReader.dateNameList.append(Latestdate)
    fileReader.numberList.append(int(infoList[0].text))

#设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#设置窗口大小
plt.figure(figsize=(12,7))

#基础数据
days = npy.array(fileReader.dateList)
daysname = fileReader.dateNameList
num  = npy.array(fileReader.numberList)

#绘制折线图并设置点标，设置标题、X坐标、y坐标
plt.plot(days,num,'r.-',label = "感染人数",marker='o', markerfacecolor='red',markersize=4)
plt.title("2019-nCoV病毒情况",fontsize=16)
plt.xticks(days,daysname,rotation=30)
plt.xlabel("日期(时间为24点)", fontsize=14)
plt.ylabel("确诊人数", fontsize=14)

#设置点y坐标
for a, b in zip(days, num):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)

#画！
plt.show()

#保存文件
with open("./Date_info.txt","w") as saveDate :
    for dateInfo in fileReader.dateList :
        saveDate.write(str(dateInfo)+" ")
    

with open("./Date_name_info.txt", "w", encoding='utf-8') as saveDateName :
    for dateNameInfo in fileReader.dateNameList :
        saveDateName.write(str(dateNameInfo)+" ")

with open("./Numb_info.txt","w") as saveNumber :
    for number in fileReader.numberList :
        saveNumber.write(str(number)+" ")