# Main Program
from register import *
from bank import *

status = False

print("Welcome to Niru Banking")

# Main Sign-Up/Sign-In Loop
while True:
    try:
        register_input = input("1. SignUp\n"
                               "2. SignIn\n"
                               "Type 'quit' to exit: ")

        # Check if user wants to quit
        if register_input.lower() == "quit":
            print("Exiting the banking process...")
            break

        register_choice = int(register_input)

        if register_choice == 1:
            SignUp()
        elif register_choice == 2:
            user = SignIn()
            status = True
            break
        else:
            print("Please enter a valid input.")

    except ValueError:
        print("Invalid input. Please enter a number.")

# Check if user signed in successfully
if status:
    account_number = db_query(f"SELECT account_number FROM Customers WHERE username='{user}';")
    
    # Check if account_number returned any results
    if account_number:
        print(f"Your account number: {account_number[0][0]}")
        
        # Initialize Bank object once
        b_obj = Bank(user, account_number[0][0])

        # Banking Service Loop
        while status:
            print(f"Welcome {user.capitalize()}. Choose Your Banking Service:\n")
            try:
                services_input = input("1. Balance Enquiry\n"
                                       "2. Cash Withdraw\n"
                                       "3. Cash Deposit\n"
                                       "4. Fund Transfer\n"
                                       "5. Check Transaction History\n"
                                       "6. Update Account Details\n"
                                       "Type 'quit' to exit: ")

                # Check if user wants to quit
                if services_input.lower() == "quit":
                    print("Exiting the banking process...")
                    break

                service = int(services_input)

                if 1 <= service <= 6:
                    if service == 1:
                        b_obj.balanceenquiry()

                    elif service == 2:
                        while True:
                            try:
                                amount = int(input("Enter Amount to Withdraw: "))
                                b_obj.withdraw(amount)
                                mydb.commit()
                                break        
                            except ValueError:
                                print("Enter a valid number for the amount.")

                    elif service == 3:
                        while True:
                            try:
                                amount = int(input("Enter Amount to Deposit: "))
                                b_obj.deposit(amount)
                                mydb.commit()
                                break
                            except ValueError:
                                print("Enter a valid number for the amount.")

                    elif service == 4:
                        while True:
                            try:
                                receive = int(input("Enter Receiver's Account Number: "))
                                amount = int(input("Enter Amount to be transferred: "))
                                b_obj.fundtransfer(receive, amount)
                                mydb.commit()
                                print("Transaction successful.")
                                break
                            except ValueError:
                                print("Enter valid numbers for account and amount.")

                    elif service == 5:
                        transactions = b_obj.transactionhistory()
                        print(transactions)

                    elif service == 6:
                        while True:
                            detail_input = input("1. Change Password\n"
                                                 "2. Update City\n"
                                                 "3. Update Contact Number\n"
                                                 "Type 'quit' to exit: ")

                            if detail_input.lower() == "quit":
                                print("Exiting the update process...")
                                break

                            try:
                                detail = int(detail_input)

                                if detail == 1:
                                    current_password = input("Please enter your current password: ")
                                    new_password = input("Please enter your new password: ")
                                    confirm_password = input("Confirm your new password: ")

                                    if new_password == confirm_password:
                                        success = b_obj.changepassword(current_password, new_password)
                                        if success:
                                            mydb.commit()
                                            print("Password updated successfully.")
                                        else:
                                            print("Password Update Failed.")
                                    else:
                                        print("New password and confirmation do not match.")

                                elif detail == 2:
                                    current_password = input("Please enter your password: ")
                                    new_city = input("Enter your new city: ")
                                    success = b_obj.changecity(current_password,new_city)
                                    if success:
                                            mydb.commit()
                                            print("City updated successfully.")
                                    else:
                                        print("City Update Failed.")

                                elif detail == 3:
                                    current_password = input("Please enter your password: ")
                                    new_contact = input("Enter your new contact number: ")
                                    if new_contact.isdigit() and len(new_contact)==10:
                                        success=b_obj.changecontact(current_password,new_contact)
                                        if success:
                                                mydb.commit()
                                                print("Contact Number Updated Successfully!")
                                        else:
                                            print("Contact Number Update Failed.")
                                        
                                    else:
                                        print("Please enter a 10-digit contact number.")
                                else:
                                    print("Invalid option. Choose between 1-3.")

                                

                            except ValueError:
                                print("Enter a valid option number.")

                else:
                    print("Please enter a valid service number.")

            except ValueError:
                print("Invalid input. Please enter a number.")


