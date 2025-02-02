# file=open("my_file.txt")
# print(file.read())
# file.close()

# # alternative to above
# mode append=a,write=w,read=r
with open("my_file.txt",mode='w') as file:
    file.write(" Piyush")