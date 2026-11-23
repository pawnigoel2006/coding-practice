expenses=[]
while True:
    print("Expense Tracker:")
    print("1. Add an expense")
    print("2. View all Expenses")
    print("3. Calculate Total Expenses")
    print("4. Search Expenses by Category")
    print("5. Exit")
    try:
        choice=int(input("Enter your choice:"))
    except ValueError:
        print("Invalid input! Please enter a number between 1 to 5.")
        continue
    if choice<=0 or choice>5:
        print("Please choose from 1 to 5")
        continue
    if choice==1:
        try:
            amount=float(input("Enter the amount:"))
        except ValueError:
            print("Enter a valid amount")
            continue
        if amount<=0:
            print("Amount must be greater than 0.")
        else:
            category=input("Enter the category: ")
            description=input("Enter the description: ")
            expenses.append({"amount":amount,"category":category,"description":description})
            print("Expense added successfully!!")
    elif choice==2:
        if len(expenses)==0:
            print("No expenses record available.")
        else:
            print("Your Expenses:")
            for index,expense in enumerate(expenses):
                print(f"{index+1}.Amount: {expense['amount']}")
                print(f"  Category: {expense['category']}")
                print(f"  Description: {expense['description']}")
    elif choice==3:
        if len(expenses)==0:
            print("No expense record available.")
        else:
            total=sum(expense["amount"] for expense in expenses)
            print(f"Total Expenses: ₹{total}")
    elif choice==4:
        found=False
        category=input("Enter the category to search:")
        for expense in expenses:
            if expense["category"].lower()==category.lower():
                print(f"Amount:{expense['amount']}")
                print(f"Description:{expense['description']}")
                found=True
        if not found:
            print("Category not found")
    elif choice==5:
        print("Thank you for using Expense Tracker. Goodbye!!")
        break