import sqlite3

import Table

conn = sqlite3.connect('banking.db')


greetingMsg = print("Welcome to the Bank!")


def display_menu():
  while True:
    print("1. Make Account")
    print("2. Delete Account")
    print("3. Modify account Information")
    print("4. Make a Deposit")
    print("5. Make a withdrawal")
    print("6. Check Balance")
    print("7. Exit")

    choice = input("Please input an option: ")

    #choice for make account
    if choice == "1":
      full_name = input("Please enter your full name: ")
      age = int(input("Enter your age:"))
      email = input( "Enter your email: ")
      password = input("Enter your password: ")
      address = input("Enter your address: ")
      phone_number = input("Enter your phone number: ")
      account_type = input("Enter your account type: ")
      account_balance = input("Enter your account balance: ")


      # Error arguement message missing??
      Table.create_account(full_name, age, email, password, address, phone_number, 
                           account_type, account_balance)

    #choice for elete account 
    elif choice == "2":
      email = input("Enter your email: ")
      password = input("Enter your password: ")
      Table.delete_account(email, password)

    
    #choice for modify acct
      email = input("Enter your email: ")
      password = input("Enter your password: ")
      update = input("Enter the field you would like to update: ")
      new_info = input(f"Enter new value for {update}: ")
      Table.modify_account(email, password, update, new_info)

    #choice for deposit
    elif choice == "4":
      id = input("Enter your ID: ")
      amount = int(input("Enter the amount you would like to deposit: "))
      Table.make_deposit(id, amount)

    #choice for withdrawal
    elif choice == "5":
      id = input("Enter your ID: ")
      amount = int(input("Enter the amount you would like to withdraw: "))
      Table.make_withdrawl(id, amount)
      
    #choice for balance
    elif choice == "6":
      id = input("Enter your ID: ")
      Table.check_balance(id)

    #choice for exit 
    elif choice == "7":
      print("Thank you for stopping by!")
      break
      
    else:
      print("ERROR. Invalid Choice. Please try again.")

conn.close()

def check():
  Table.check_table_values('registration')
  Table.check_table_values('transactions')
  
if __name__ == "__main__":
  display_menu()
#check()





    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    





