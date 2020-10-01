#driver code
ab = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
def encode():
    message = input("enter the message you want to encode").lower()
    sc = int(input("enter the shift no."))
    new_message = ""
    for letter in message:
        i = ab.index(letter)
        i += sc
        if i>=26:
            i -= 26            #code contributed by prankit!!!!
        new_message += ab[i]
    return f"the encode message with shift code:{sc} is {new_message}"
def decode():
    message = input("enter the messsage you want to decode").lower()
    sc = int(input("enter the shift no."))
    new_message = ""
    for letter in message:
        i = ab.index(letter)
        i -= sc
        if i<0:
            i += 26
        new_message += ab[i]
    return f"the decode message with shift code:{sc} is {new_message}"

print("WELCOME TO TH SHIFT CODE")
while 1:
    print("------------------------------------------------------------------------------------------------------")
    print("'''MENU'''")
    print("1. MAKE A CODE...\n2. DECODE A MESSAGE...\n3. QUIT")
    uc = int(input("enter choice"))
    if uc==1:
        print(encode())
    elif uc==2:
        print(decode())
    elif uc==3:
        exit()
    else:
        print("invalid option")
