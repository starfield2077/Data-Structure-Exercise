import csv
dic = {}
with open("nyc_weather.csv", 'r') as myFile:
    reader = csv.reader(myFile)
    data = [row for row in reader]
    for index in range(1, len(data)):
        dic.update({data[index][0]:int(data[index][1])})

aver_temp = 0
max_temp = 0
key = 'Jan '
day = 0
print(dic)
for i in range(1,8):
    print("Jan " + str(i) + "'s temperature is " + str(dic[key + str(i)]))
    aver_temp += dic[key + str(i)] / 7
print("average temperature of first week in January is: " + str(aver_temp) + '\n')

for i in range(1,11):
    if dic[key + str(i)] >= max_temp:
        max_temp = dic[key + str(i)]
        day = str(i)

print("maximum temperature in first 10 days in January is: " + str(max_temp) + " and it's on: " + str(key + day) + '\n')

print("temperature on Jan 9 is: " + str(dic['Jan 9']))
print("temperature on Jan 4 is: " + str(dic['Jan 4']))
