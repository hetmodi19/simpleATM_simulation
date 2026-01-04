balance = 10000  # initial balance

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        print("Your current balance is:", balance)

    elif choice == 2:
        deposit = int(input("Enter amount to deposit: "))
        if deposit > 0:
            balance += deposit
            print("Amount deposited successfully.")
            print("Updated balance:", balance)
        else:
            print("Invalid deposit amount.")

    elif choice == 3:
        withdraw = int(input("Enter amount to withdraw: "))
        if withdraw <= balance and withdraw > 0:
            balance -= withdraw
            print("Please collect your cash.")
            print("Updated balance:", balance)
        else:
            print("Insufficient balance or invalid amount.")

    elif choice == 4:
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
