print("Calculator APP")

while True :
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Square")
    print("6.Exit")

    choice = int(input("Enter your choice(1-6):  "))

    if (choice== 6) :
        print("Exiting...")
        break

    elif (choice ==5):
        num =float(input("Enter your number:  " ))
        print("Result= ",num**2)

    elif choice in [1,2,3,4]:
         num1 = float(input("Enter your first number:  "))
         num2 = float(input("Enter your second number:  "))

    if choice==1:
        print(num1+num2)
    elif choice==2:
        print(num1-num2)
    elif choice==3:
        print(num1*num2)
    elif choice==4:
        if num2==0:
            print("Cannot divide by zero")
        else:
            print(num1/num2)

    else:
        print("Invalid Input")

