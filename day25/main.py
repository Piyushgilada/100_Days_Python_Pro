# import csv
# with open('/Users/piyush/python/piyush/pythonProject/day25/weather_data.csv') as data_file:
#     data=csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1]!= "temp":
#             temperature.append(int(row[1]))
#     print(temperature)
import pandas
# import pandas as pd
#
# file = pd.read_csv('/Users/piyush/python/piyush/pythonProject/day25/weather_data.csv')
# print(file)
# print(type(file))
# print(type(file['day']))
# print(file.to_dict())
# temp_list = file['temp'].to_list()
# print(file['temp'].abs())

# print(file['condition'])   # here we treat file as dictionary and access by 'condition' i.e key
# print(file.temp)  # here we are getting file object and attribute temp


# max_temp_record = file[file.temp == max(file.temp)]
# print(max_temp_record.temp * 9 / 5 + 32)
# dic={'name':['h1','h2','h3'],
#      'score':[89,98,79]}
# data=pd.DataFrame(dic)
# print(data)

import pandas as pd
data=pd.read_csv('/Users/piyush/python/piyush/pythonProject/day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250116.csv')
grey_squarel_count=len(data[data['Primary Fur Color'] == 'Gray'])
red_squarel_count=len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squarel_count=len(data[data['Primary Fur Color'] == 'Black'])
print(grey_squarel_count)
print(red_squarel_count)
print(black_squarel_count)
data_dict={
    "Fur Color":["Gray","Cinnamon","Black"],
    "count":[grey_squarel_count,red_squarel_count,black_squarel_count]
}
df=pandas.DataFrame(data_dict)
df.to_csv("short_data_for_Fur_Colorx")