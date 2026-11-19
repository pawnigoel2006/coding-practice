while True:
    try:
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        continue
    print("Select operation:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    choice=input("Enter choice(1/2/3/4):")
    if choice=='1':
        print(num1,"+",num2,"=",num1+num2)
    elif choice=='2':
        print(num1,"-",num2,"=",num1-num2)
    elif choice=='3':
        print(num1,"*",num2,"=",num1*num2)
    elif choice=='4':
        if num2==0:
            print("Error! Division by zero.")
        else:
            print(num1,"/",num2,"=",num1/num2)
    else:
        print("Invalid input")
    while True:
        next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if next_calculation == "yes":
            break
        elif next_calculation == "no":
            print("Bye!!")
            exit()
        else:
            print("Invalid choice! Please enter yes or no.")