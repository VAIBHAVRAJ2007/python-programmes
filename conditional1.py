age=int(input("Enter your age:"))
if(age>=18):
    if(age>85 and age<110): #nested if
        print("Can't drive")
    elif(age>=110):
        print("You are too young")
    else:
        print("Can drive")
else:
    print("Can't drive")