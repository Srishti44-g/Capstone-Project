while 1:
    print(" WELCOME TO THE SHIFT CODE\n ")
    print("1) Make a code.\n2) Decode a message.\n3) Quit.\n")
    code = int(input("Enter the choice : "))
    alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    if code == 1:
        message = input("Enter the message you want to encode: ")
        shiftc = int(input("Enter the shift no. : " ))
        new_mess = ""
        for letter in message:
            i = alpha.index(letter)
            i += shiftc
            if i >= 26:
                i -= 26
            new_mess += alpha[i]
        
        print(f"The encoded message with shift code: {shiftc} is {new_mess}\n\n")

    elif code == 2:
        message = input("Enter the message you want to encode: ")
        shiftc = int(input("Enter the shift no. : " ))
        new_mess = ""
        for letter in message:
            i = alpha.index(letter)
            i -= shiftc
            if i < 0:
                i += 26
            new_mess += alpha[i]
            
        print(f"The decoded message with shift code: {shiftc} is {new_mess}\n\n")   

    elif code == 3:
        exit ()

    else :
        print("Invalid option... please enter again!")
