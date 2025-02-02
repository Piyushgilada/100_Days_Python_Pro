# '''
# Q.1 How can a number be expressed as a sum of two prime numbers?
# Write a Program
# '''
# import math
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# def find_prime_sum(n):
#     for i in range(2, n//2 + 1):
#         if is_prime(i) and is_prime(n - i):
#             return f"{n} can be expressed as the sum of {i} and {n - i}."
#     return f"{n} cannot be expressed as the sum of two prime numbers."
# number=34
# print(find_prime_sum(number))
#

''' Q.2 How to Check Whether a Number is a Perfect Number or not?
# Write a Program
# '''
#
# n = 28
# if is_perfect(n):
# result = f"{n} is a perfect number."}}
# else:
#     result = f"{n} is not a perfect number."
# result

# '''output : 28 is a perfect number because its divisors are 1, 2, 4, 7, and 14, and the sum of these divisors'''

''' There is a list of decimal numbers, as well as an infection that has a specific amount of
spikes. Each spike represents the amount of binary digits that a virus will eat from the
right-hand part of a decimal number. Write a program that will determine the final status
of each number following the virus that has consumed the specified amount of binary
digits from each one of them.'''
# N = int(input('no of items : '))
# a = list(map(int, input("enter list: ").split(',')))
# n = int(input('spikes : '))
# result = " ".join(str(i >> n) for i in a)
# print(result)


''' Q.4 Can You Write a program that takes a string containing multiple
words as input? Sort these words in ascending order alphabetically.
Then, print all the words that start with a vowel, along with their
positions in the sorted list. '''
#
# string1='apple banana cherry orange mango'
# string1.lower()
# list=string1.split(' ')
# list.sort()
# print(list)
# vowel=['a','e','i','o','u']
# for index in range(len(list)):
#     if list[index][0] in vowel:
#         print(f'{index}:{list[index]}')

''' After JEE Mains, students have been admitted to an engineering college, forming a class of 'n'
students. The Head of the Department (HOD) is tasked with selecting a class monitor. However,
the HOD meets the students one by one and has a peculiar way of choosing. Each time the
HOD meets a student, if the student's rank is lower than that of the previous student met, the
HOD cuts the previous student's name and writes the new student's name along with their rank
in a register. Given the ranks the HOD receives each time they meet a student, predict how
many names are cut from the list '''
# list=[5,8,6,3,9,4,2]
# max_rank=0
# cut_count=0
# for i in list:
#     if i > max_rank:
#         max_rank=i
#         cut_count+=1
# print(cut_count)

# N = int(input())
# ranks = list(map(int, input().split()))
# cuts = 0
# prev_rank = ranks[0]
# for rank in ranks[1:]:
#     if rank < prev_rank:
#         cuts+=1
#         prev_rank=rank
#
# print(cuts)


''' Rahul is known for copying in exams from his adjacent students, but he's smart about it. Instead
of directly copying the words, he changes the positions of letters while keeping the letters
constant. As the examiner, you need to determine if Rahul has copied a certain word from the
adjacent student who is giving the same exam. You should provide Rahul with the appropriate
markings based on your findings.'''

# original =input("enter string").lower()
# rahul_copy = input('enter string').lower()
# if sorted(original)==sorted(rahul_copy):
#     print(True)



''' Anirudh is attending an astronomy lecture, but he's struggling with understanding the material.
His professor, who is very strict, asks students to write a program to print a trapezium pattern
using stars (*) and dots (.) as shown below. Since Anirudh is not proficient in astronomy, can
you help him '''

# N = int(input())
# for i in range(N):
#     for j in range(N * 2):
#         if j < N - i or j >= N + i + 1:
#             print(" " ,end="")
#         else:
#             print("_",end="")
#     print()

# sub_arr_length=int(input("enter length of subarray"))
# list=[3,1,4,6,2,5]
# list1=[]
# max=list[0]
# min=list[1]
#
# for i in range(len(list)):
#     if i+1 <sub_arr_length:
#         list1.append(list[i])
# print(list1)

# def funa(a,b):
#     if b==0:
#         return 1
#     if b%2==0:
#         return funa((a*a),(b/2))
#     return funa(a=(a*a*a),b=((b/2)*a))
#
# result=funa(2,4)
# print(result)

n,x=map(int,input().split())
position=x%n
if position ==0:
    position=n
print(position+1)

