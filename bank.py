# BANKING SERVICES
from database import *
import datetime

class Bank:
    def __init__(self, username, account_number):
        self.__username = username
        self.__account_number = account_number

    def create_transaction_table(self):
        db_query(f"CREATE TABLE IF NOT EXISTS {self.__username}_Transaction "
                 f"(timedate VARCHAR(30), "
                 f"account_number INT, "
                 f"remarks VARCHAR(30), "
                 f"amount INT);")


    def balanceenquiry(self):
        temp= db_query(f"SELECT balance FROM Customers WHERE username='{self.__username}';")
        print(f"Your Current Balance is {temp[0][0]}")   

    def deposit(self,amount):
        temp = db_query(f"SELECT balance FROM Customers WHERE username='{self.__username}';")
        test = amount + temp[0][0]
        #temp[0][0]+=amount
        db_query(f"UPDATE Customers SET balance={test} WHERE username='{self.__username}';" )
        #self.balanceenquiry()
        db_query(f"INSERT INTO {self.__username}_Transaction VALUES ("
                 f"'{datetime.datetime.now()}',"
                 f"{self.__account_number},"
                 f"'Amount Deposit',"
                 f"{amount});")
        print(f"Dear {self.__username}, Amount {amount} is successfully deposited into your account {self.__account_number}.")
        
    def withdraw(self,amount):
        temp = db_query(f"SELECT balance FROM Customers WHERE username='{self.__username}';")
        if amount > temp[0][0]:
            print("Insufficient Balance. Please Deposit Money.")
        else:
            test = temp[0][0]-amount
            #temp[0][0]-=amount
            db_query(f"UPDATE Customers SET balance={test} WHERE username='{self.__username}';" )
            #self.balanceenquiry()
            db_query(f"INSERT INTO {self.__username}_Transaction VALUES ("
                        f"'{datetime.datetime.now()}',"
                        f"{self.__account_number},"
                        f"'Amount Withdraw',"
                        f"{amount});")
            print(f"Dear {self.__username}, Amount {amount} is successfully withdrawn from your account {self.__account_number}.")

        
    def fundtransfer(self,receive,amount):
        temp  = db_query(f"SELECT balance FROM Customers WHERE account_number={self.__account_number};")
        if amount > temp[0][0]:
            print("Insufficient Balance. Please Deposit Money.")
        else:
            temp2  = db_query(f"SELECT balance FROM Customers WHERE account_number={receive};")
            test = temp[0][0]-amount
            test2 = temp2[0][0]+amount
            #temp[0][0]-= amount
            #temp2[0][0]+= amount
            db_query(f"UPDATE Customers SET balance={test} WHERE account_number={self.__account_number};")
            db_query(f"UPDATE Customers SET balance={test2} WHERE account_number={receive};")
            receiver_username = db_query(f"SELECT username FROM Customers WHERE account_number={receive};")[0][0]
            db_query(f"INSERT INTO {receiver_username}_Transaction VALUES ("
                        f"'{datetime.datetime.now()}',"
                        f"{receive},"
                        f"'Fund Transferred by {self.__username}',"
                        f"{amount});")
            db_query(f"INSERT INTO {self.__username}_Transaction VALUES ("
                        f"'{datetime.datetime.now()}',"
                        f"{self.__account_number},"
                        f"'Fund Transferred to {receiver_username}',"
                        f"{amount});")
            print(f"Dear {self.__username}, Amount {amount} has been successfully transferred to Acc.No.: {receive}")

    def transactionhistory(self):
        print(f"Executing query for user: {self.__username}")
        return db_query(f"SELECT * FROM {self.__username}_Transaction; ")
    
    def changepassword(self,current_password,new_password):
        password = db_query(f"SELECT password FROM Customers WHERE username = '{self.__username}';")[0][0]
        if current_password == password:
            db_query(f"UPDATE Customers SET password='{new_password}' WHERE username='{self.__username}';")
            return True
        else:
            print("Wrong current password entered. Try again.")
            return False
            
    def changecity(self,current_password,new_city):
        password = db_query(f"SELECT password FROM Customers WHERE username = '{self.__username}';")[0][0]
        if current_password == password:
            db_query(f"UPDATE Customers SET city='{new_city}' WHERE username='{self.__username}';")
            return True
        else:
            print("Wrong password entered. Try again.")
            return False
        
    def changecontact(self,current_password,new_contact):
        password = db_query(f"SELECT password FROM Customers WHERE username = '{self.__username}';")[0][0]
        if current_password == password:
            db_query(f"UPDATE Customers SET contact_number='{new_contact}' WHERE username='{self.__username}';")
            return True
        else:
            print("Wrong password entered. Try again.")
            return False

    


        
