import csv
file = open("info.csv", "w")
newRecord = "sRISHTIg0234#\n"
file.write(str(newRecord))
file.close()
# driver code
def passwordf():
    print("RULES FOR WRITING A PASSWORD")
    cmt = '''             1. it should have at least 8 characters;
             2.it should include uppercase letters;
             3.  it should include lower case letters;
             4. it should include numbers; and
             5. it should include at least one special character such as !, £, $, %, &, <, * or @. 
           '''
    print(cmt)
    pw = input("enter the password: ")
    score = 0
    for i in pw:
        if len(pw) >= 8:
            score += 1
        elif i.isupper():
            score = + 1
        elif i.islower():
            score += 1
        elif i.isalnum():
            score += 1
        elif i in ["!", "£", "$","%", "&", "<", "*", "@"]:
            score += 1

    if score == 2 or score == 1:
        print("password too weak try again setting a new password")
    elif score == 3 or score == 4:
        print("moderate password try again")
    else:
        print("strong password confirmed")
        return (pw + "\n")


def get_id():
    newid = input("enter a new username")
    with open("info.csv", "r") as file:
        reader = csv.reader(file)
        temp = list(reader)
        for i in range(len(temp)):
            if newid != temp[i][0]:
                print("ok its a unique id")
                password = passwordf()
                with open("info.csv", "w") as file:
                    newrecord = newid + "," + password
                    file.write(str(newrecord))
                    print("!!!! hurray your id is created !!!!!")
            else:
                print("sorry the username already exixts")


def chng_pass():
    uid = input("enter the username of the id you want to change the password: ")
    with open("info.csv", "r") as file:
        reader = csv.reader(file)
        temp = list(reader)
        for i in range(len(temp)):
            if uid in temp[i][0]:
                password = passwordf()       
                temp[i][1] = password
                print("password successfully changed")
            else:
                print("sorry the id you are searching for is invalid")



def disp():
    with open("info.csv","r") as file:
        reader = csv.reader(file)
        temp = list(reader)
        print("!!!!this is the list of stored usernames!!!!")
        print(temp)
        for i in range(len(temp)):
            print(f"{i+1}.{temp[i][0]}")

#main.......
print("WELCOME TO THE PASSWORD PROGRAM")
while 1:
    print("MENU")
    print("1. GET NEW USER ID: \n2. CHANGE A PASSWORD: \n3. DISPLAY ALL USER ID: \n4. QUIT: ")
    uc = int(input("enter the choice: "))
    if uc == 1:
        print(get_id())
    elif uc == 2:
        print(chng_pass())
    elif uc == 3:
        print(disp())                   
    elif uc == 4:
        exit()
    else:
        print("invalid user choice")
