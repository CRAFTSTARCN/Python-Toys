#File reader
print("正在读取历史信息")
import datetime
import time
import sys

if __name__ == "__main__":
    print("这是文件操作模块，请在main.py中启动")
    quit()

dateList     = list()
dateNameList = list()
numberList   = list()
nowDatetime  = datetime.datetime(int(time.strftime("%Y")),int(time.strftime("%m")),int(time.strftime("%d")))

historyTimeList = list()
with open("./Last_Date.txt",'r') as lastDateFile:
    historyTimeList = lastDateFile.readline().split(" ")

lastTime = datetime.datetime(int(historyTimeList[0]), int(historyTimeList[1]), int(historyTimeList[2]))
diff = nowDatetime - lastTime
diff_int = int(diff.days)

with open("./Date_info.txt","r") as dateFile:
    line = dateFile.readline().strip()
    while line:
        dataLine = line.split(" ")
        dateList = dateList + dataLine
        line = dateFile.readline().strip()

with open("./Date_name_info.txt", "r", encoding='utf-8') as dateNameFile:
    line = dateNameFile.readline().strip()
    while line:
        dataNameLine = line.split(" ")
        dateNameList = dateNameList + dataNameLine;
        line = dateNameFile.readline().strip()

with open("./Numb_info.txt", "r", encoding='utf-8') as numberFile:
    line = numberFile.readline().strip()
    while line:
        dataNumberLine = line.split(" ")
        numberList = numberList + dataNumberLine;
        line = numberFile.readline().strip()

dateList_numb = list()
for date in dateList :
    dateList_numb.append(int(date))
numberList_numb = list()
for number in numberList :
    numberList_numb.append(int(number))

dateList = dateList_numb
numberList = numberList_numb

if dateList.__len__() == dateNameList.__len__() and dateList.__len__() == numberList.__len__():
    print("文件读取成功")
else:
    raise EnvironmentError("文件已经损坏")

print("更新日期")
with open("./Last_Date.txt","w") as updateFile :
    updateFile.write(time.strftime("%Y")+" "+time.strftime("%m")+" "+time.strftime("%d"))
print("更新完成")