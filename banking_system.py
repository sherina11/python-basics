balance = 0

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = int(input("Enter amount to deposit: "))
        balance = balance + amount
        print("Amount deposited successfully")

    elif choice == "2":
        amount = int(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance = balance - amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    elif choice == "3":
        print("Current Balance:", balance)

    elif choice == "4":
        print("Thank you for using the banking system")
        break

    else:
        print("Invalid choice")