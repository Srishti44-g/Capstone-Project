import random

count3=0
while True :
    list = ["blue","pink","green","red","white","black","yellow","orange","black"]
    sample=random.choices(list,k=4)
    color=[]
    count1=0
    count2=0
    count3=count3+1
    print(list)
    for i in range(4):
        c=input("Enter a color : ")
        color.append(c)
    for i in range(4):
        if(sample[i]==color[i]):
            count1=count1+1
        else:
            for j in range(4):
                if(sample[i]==color[j]):
                    count2=count2+1
                    break
    print(f"Correct color in the correct place {count1}")
    print(f"Correct color but in the wrong place {count2}")
    if(count1==4):
        break
print(f"You took {count3} guesses.")
