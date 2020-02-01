import matplotlib.pyplot as plt 
import numpy as npy 
import fileReader
import grabber
import time
from scipy.interpolate import*

#时间对照表
monthTransfer = {1:"一",2:"二",3:"三",4:"四",5:"五",6:"六",7:"七",8:"八",9:"九",10:"十",11:"十一",12:"十二"}

#获取爬虫数据
conf = int(grabber.findData("confirmedCount"))
susp = int(grabber.findData("suspectedCount"))
cure = int(grabber.findData("curedCount"))
dead = int(grabber.findData("deadCount"))

print("确诊：",conf,"疑似：",susp,"治愈：",cure,"死亡：",dead)

#预处理，检测是否已经过了一天,并更新数据
month = int(time.strftime("%m"))
Latestdate = monthTransfer[month]+"月"+time.strftime("%d")+"至"+time.strftime("%H")+"H"
if fileReader.diff_int == 0 :
    fileReader.numberList[-1]   = conf
    fileReader.dateNameList[-1] = Latestdate
else:
    fileReader.dateList.append(fileReader.dateList[-1]+fileReader.diff_int)
    fileReader.dateNameList.append(Latestdate)
    fileReader.numberList.append(conf)

#设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#设置窗口大小
plt.figure(figsize=(12,8))

#基础数据
days = npy.array(fileReader.dateList)
daysname = fileReader.dateNameList
num  = npy.array(fileReader.numberList)

#差分数据
diffList = list()
for i in range(1,fileReader.numberList.__len__()) :
    diffList.append(fileReader.numberList[i] - fileReader.numberList[i-1])
diffArray = npy.array(diffList)

#绘制全国折线图并设置点标，设置标题、X坐标、y坐标
plt.subplot(211)
plt.plot(days,num,'r.-',label="确诊人数", marker='o', markerfacecolor='red', markersize=4)
plt.plot(days[1:],diffArray,'y.-',label="增加病例", marker='o', markerfacecolor='yellow', markersize=4)
plt.title("2019-nCoV病毒情况", fontsize=16)
plt.xticks(days,daysname, rotation=30, fontsize='8')
plt.ylabel("人数", fontsize=14)
plt.legend()
##设置点y坐标
for a, b in zip(days, num):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=8)
for c, d in zip(days[1:], diffArray):
    plt.text(c, d, d, ha='center', va='bottom', fontsize=8)

#绘制各个省图片
plt.subplot(212)
plt.bar(grabber.provNames, grabber.provNumber)

##设置标签
plt.xticks(fontsize = 8, rotation=30)
plt.ylabel("人数", fontsize=14)
plt.xlabel("图一：日期(未标注为24时)与确诊/新增人数 图二：各省确诊人数", fontsize=12)
##标上数据
for e, f in zip(grabber.provNames, grabber.provNumber):
    plt.text(e, f, f, ha='center', va='bottom', fontsize=8)

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

#画！
plt.show()