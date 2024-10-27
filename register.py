# Driver code for Sign in/Sign Up

from database import *
from customer import *
from bank import *
import random

def SignUp():

    username = input("Create Username (or type 'quit' to exit): ")
    if username.lower() == "quit":
        print("Exiting sign-up process.")
        return

    cursor.execute("SELECT username FROM Customers WHERE username = %s", (username,))
    temp = cursor.fetchone()
    
    if temp:
        print(f"Username '{username}' is already taken.")
        SignUp()
    else:
        print(f"Username '{username}' is available. Please Proceed.")
        
        password = input("Enter your Password (or type 'quit' to exit): ")
        if password.lower() == "quit":
            print("Exiting sign-up process.")
            return

        name = input("Enter your Name (or type 'quit' to exit): ")
        if name.lower() == "quit":
            print("Exiting sign-up process.")
            return

        while True:
            age_input = input("Enter your Age (or type 'quit' to exit): ")
            if age_input.lower() == "quit":
                print("Exiting sign-up process.")
                return
            try:
                age = int(age_input)
                break
            except ValueError:
                print("Please enter a valid age (a number).")

        city = input("Enter your City (or type 'quit' to exit): ")
        if city.lower() == "quit":
            print("Exiting sign-up process.")
            return
        
        while True:
            contact_input = input("Enter your contact number (or type 'quit' to exit): ")
            if contact_input.lower() == "quit":
                print("Exiting sign-up process.")
                return
            try:
                if contact_input.isdigit() and len(contact_input)==10:
                    contact_number = int(contact_input)
                    break
                else:
                    print("Enter a 10-digit number.")
                    continue
            except ValueError:
                print("Enter a valid number.")

        while True:
            account_number = random.randint(10000000, 99999999)
            temp = db_query(f"SELECT account_number FROM Customers WHERE account_number={account_number};")
            if not temp:
                print("Your Account Number is: ", account_number)
                break
        
        # Create customer object
        c_obj = Customer(username, password, name, age, city, contact_number, account_number)
        c_obj.createuser()

        # Create bank object
        b_obj = Bank(username,account_number)
        b_obj.create_transaction_table()
        

def SignIn():
    username = input("Enter Username: ")
    temp = db_query(f"SELECT username FROM Customers WHERE username='{username}';")
    
    if temp:
        while True:
            password = input(f"Welcome '{username.capitalize()}'. Please enter Password (or type 'quit' to exit): ")
            
            # Check if the user wants to exit
            if password.lower() == "quit":
                print("Exiting the banking process.")
                return
            
            # Verify password
            temp = db_query(f"SELECT password FROM Customers WHERE username='{username}';")
            if temp[0][0] == password:
                print("Signed IN Successfully!")
                return username  # Return username on successful login
            else:
                print("Wrong password. Try again.")
    else:
        print("Username does not exist")
        SignUp()
