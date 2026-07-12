balance = 0

def deposit():
    global balance
    amount = float(input("Deposit Amount: "))
    print(f"\n✅ {amount} deposited successfully.")
    balance += amount

def withdraw():
    global balance

    amount = float(input("Withdraw Amount: "))

    if amount <= balance:
        balance -= amount
        print(f"{amount} withdraw successfully.")
    
    else: 
        print(f"Insufficient balance")


def check_balance():
    global balance
    print(f"\n💰 Current Balance: {balance}")

while True:

    print("\n======Bank Account=======")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        deposit()
    
    elif choice == 2:
        withdraw()
    
    elif choice == 3:
        check_balance()
    
    elif choice == 4:
        print("Thank You.")
        break
    else:
        print("Invalid choice.")
