class Account:
    def __init__(self, account_number, holder_name, initial_deposit):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = initial_deposit

    def deposit(self, amount):
        self.balance+=amount
        print(f"Deposited amount {amount}. New Balance is {self.balance:.2f}")
        
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdraw amount {amount}. New Balance is {self.balance:.2f}")
            
    def check_balance(self):
        print(f"Your Current Balance is {self.balance:.2f}")

    def display_account_details(self):
        print(f"\nAccount Number: {self.account_number}")
        print(f"Account Holder: {self.holder_name}")
        print(f"Account Balance: ${self.balance: .2f}")

def main():
    accounts={}

    while True:
        print("\n===Simple Banking System===")
        print("1. Create Account")
        print("2. View Account Details")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Check Balance")
        print("6. Exit")
        choice=input("Enter Your Choice:")

        if choice == '1':
            account_number = input("Enter Account Number: ")
            holder_name = input("Enter Account Holder Name: ")
            initial_deposit = float(input("Enter Initial Deposit: "))
            accounts[account_number] = Account (account_number, holder_name, initial_deposit)
            print("Account Created Successfully!")

        elif choice == '2':
            account_number = input("Enter Account Number: ")
            if account_number in accounts:
                accounts[account_number].display_account_details()
            else:
                print("Account Not Found!")

        elif choice == '3':
            account_number = input("Enter Your Account Number: ")
            if account_number in accounts:
                amount = float(input("Enter Amount To Deposit: "))
                accounts[account_number].deposit(amount)
            else:
                print("Account Not Found!")

        elif choice == '4':
            account_number = input("Enter Account Number: ")
            if account_number in accounts:
                amount = float(input("Enter Amount To Withdraw: "))
                accounts[account_number].withdraw(amount)
            else:
                print("Account Not Found!")

        elif choice == '5':
            account_number = input("Enter Account Number: ")
            if account_number in accounts:
                accounts[account_number].check_balance()
            else:
                print("Account Not Found!")

        elif choice == '6':
            print("Thank you for using the Banking System!")
            break

        else:
            print("Invalid choice! Please try again later.")

if __name__ == '__main__':
    main()



