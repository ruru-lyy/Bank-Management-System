# Customer Details
from database import *

class Customer:
    def __init__(self,username,password,name,age,city,contact_number,account_number):
        self.__username=username
        self.__password= password
        self.__name = name
        self.__age = age
        self.__city = city
        self.__contact_number = contact_number
        self.__account_number = account_number

    def createuser(self):
        temp  =db_query(f"INSERT INTO Customers VALUES ('{self.__username}','{self.__password}','{self.__name}',{self.__age},'{self.__city}',{self.__contact_number},0,{self.__account_number},True);")
        mydb.commit()