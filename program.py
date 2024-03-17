
import os
import csv
from datetime import datetime

def main():
    print("Pinance Lite.")
    checking_balance = 0
    savings_balance = 0
    purchase_total = 0

    while True:
        print("\nChoose one of the following options:")
        print("1. View current balances")
        print("2. Deposit to checking account")
        print("3. Withdraw from checking account")
        print("4. Transfer from savings to checking")
        print("5. Add purchases")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            print(f"Checking balance: ${checking_balance:.2f}")
            print(f"Savings balance: ${savings_balance:.2f}")
        elif choice == '2':
            deposit = float(input("Enter the deposit amount: $"))
            checking_balance += deposit
            print(f"New checking balance: ${checking_balance:.2f}")
        elif choice == '3':
            withdraw = float(input("Enter the withdrawal amount: $"))
            checking_balance -= withdraw
            print(f"New checking balance: ${checking_balance:.2f}")
        elif choice == '4':
            transfer = float(input("Enter the transfer amount from savings to checking: $"))
            savings_balance -= transfer
            checking_balance += transfer
            print(f"New checking balance: ${checking_balance:.2f}")
        elif choice == '5':
            purchase = float(input("Enter the purchase amount: $"))
            purchase_total += purchase 
        elif choice == '6':
            print("Exiting the program. Have a great day!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

    # Write output to a file
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_filename = f"{output_folder}/output-{timestamp}.txt"

    with open(output_filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Checking Balance", "Savings Balance"])
        writer.writerow([checking_balance, savings_balance])

if __name__ == "__main__":
    main()
