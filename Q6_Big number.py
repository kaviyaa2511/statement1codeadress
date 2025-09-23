numberOne=float(input("Enter a number: "))
numberTwo=float(input("Enter a number: "))
numberThree=float(input("Enter a number: "))
if numberOne>numberTwo and numberOne>numberThree:
    print("Biggest number: ",numberOne)

elif numberTwo>numberOne and numberTwo>numberThree:
    print("Biggest number: ",numberTwo)

else:
    print("Biggest number: ",numberThree)
