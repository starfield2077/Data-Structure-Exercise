import csv
dic = {}
with open("nyc_weather.csv", 'r') as myFile:
    reader = csv.reader(myFile)
    data = [row for row in reader]
    for index in range(1, len(data)):
        dic.update({data[index][0]:int(data[index][1])})

aver_temp = 0
for i in range(7):
    aver_temp += dic[i]