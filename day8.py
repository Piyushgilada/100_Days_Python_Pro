def caesar_cipher(message,operation,shift_number):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result=''
    for char in message:
        if char in alphabet:
            if operation=='encode':
                position=alphabet.index(char)
                new_position=position+shift_number
                result+=alphabet[new_position]
            elif operation=='decode':
                position=alphabet.index(char)
                new_position=position-shift_number
                result += alphabet[new_position]
        else:
            result+=char
    return result

flag='yes'
while flag=="yes":
    # get user input
    message=input("enter message ")
    operation=input("encode for encrypt and decode for decrypt").lower()
    shift_number=int(input("enter number for shifting"))
    shift_number %= 26 # Limit the shift to the range of 0-25
    result = caesar_cipher(message,operation,shift_number)
    print(f"Here is the {operation}d result: {result}")
    flag=input("do you want to go agin type yes.otherwise no").lower()



