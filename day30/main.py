# try:
#     file=open('text.txt')           # file not exist error
#     dic1={'key':'value'}            # value error
#     print(dic1['keyy'])
# except FileNotFoundError:
#     file=open('text.txt','w')
#     file.write("something")
# except KeyError as error_message:
#     print(f"the key is {error_message} not exist")
# finally:  # // jayega isme toh
#     print("finally block")

height=float(input("Enter Height "))
weight=int(input("Enter Weight "))
if height >3:
    raise ValueError('human value can not be over 3 meter')
bmi=weight / height**2
print(bmi)