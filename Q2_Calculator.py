Num1=int(input("Enter the Number 1: "))
Num2=int(input("Enter the Number 2: "))
while True:
    print("1 - Add, 2 - Sub, 3 - Mul, 4 - Div, 5 - Mod")
    oper=int(input("Enter the operation: "))
    if oper==1:
        print(Num1,"+",Num2,"=",Num1+Num2)
    elif oper==2:
        print(Num1,"-",Num2,"=",Num1-Num2)
    elif oper==3:
        print(Num1,"*",Num2,"=",Num1*Num2)
    elif oper==4:
        if Num2==0:
            print("This operation cannot be done since Num 2 is zero")
        else:
            print(Num1,"/",Num2,"=",Num1/Num2)
    elif oper==5:
        print(Num1,"%",Num2,"=",Num1%Num2)
    else:
        print("Enter Vaild Operation")
    yesNo=input("Do you want to continue (Yes/No)? ")
    if yesNo=="No":
        break
            
