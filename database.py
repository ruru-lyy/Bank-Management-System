import mysql.connector as sql 

mydb = sql.connect(
    host="localhost",
    user="root",
    passwd="Niru2001",
    database="BANK"
)

cursor= mydb.cursor()

def db_query(str):
    cursor.execute(str)
    result = cursor.fetchall()
    return result

def createcustomertable():
    cursor.execute('''
               CREATE TABLE IF NOT EXISTS Customers
               (username VARCHAR(20),
               password VARCHAR(20),
               name VARCHAR(20),
               age INT,
               city VARCHAR(20),
               contact_number BIGINT,
               balance INT,
               account_number INT,
               status BOOL
               )
               ''')

    mydb.commit()

if __name__=="__main__":
    createcustomertable()
    