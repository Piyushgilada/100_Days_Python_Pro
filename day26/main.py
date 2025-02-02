# string_1="piyush"
# new_list= [letter+"zzz" for letter in string_1]
#
# new_list1=[i for i in range(1,10) if i%2]  #list comprehension
# print(new_list1)
import random

import pandas

# names = ["alex",'barry','consa','david','muli']
# new_dict = {student:random.randint(1,100) for student in names}
# print(new_dict)
# new_dict_1= {student:value for (student,value) in new_dict.items() if value > 60}
# print(new_dict_1)


# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# list=sentence.split(' ')
# result = {letter:len(letter) for letter in list}
# print(result)

''' You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each 
temperature in degrees Celsius and converts it into degrees Fahrenheit. 
'''
# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
#
# weather_f ={day:(temperature*9/5+32) for (day,temperature) in weather_c.items()}
#
# print(weather_f)
import pandas as pd
# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
#TODO looping through dictionary
# for key,value in weather_c.items():
#     print(value)

# weather_frame = pd.DataFrame(list(weather_c.items()), columns=["Day", "Temperature"])
# print(weather_frame)
# for index,row in weather_frame.iterrows():
#     print(row.Temperature)

data=pd.read_csv('/Users/piyush/python/piyush/pythonProject/day26/nato_phonetic_alphabet.csv')
# TODO create a dictionary in this format
new_dict = {row.letter:row.code for (index,row) in data.iterrows()}
# print(new_dict)
# TODO create a list of the phonetic code words from a word that the user inputs
flag=0
while flag == 0:
    word = input("Enter a word: ").upper()
    try:
        output_list=[new_dict[letter] for letter in word]
        print(output_list)
        flag=1
    except KeyError :
        print('Only alphabets are allowed')
        print("try again")


