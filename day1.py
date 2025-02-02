import random
print("welcome to the password generator ")
l=int(input("how many letter in password"))
s=int(input("how many symbols"))
d=int(input("how many digits"))

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
symbols = '~!@#$%^&*'
digits = '0123456789'

choice_l=random.choices(letters,k=l)
choice_s=random.choices(symbols,k=s)
choice_d=random.choices(digits,k=d)

password_list=choice_l+choice_s+choice_d
random.shuffle(password_list)
password="".join(password_list)
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
print("your password is: ",password)