import sqlite3
import unittest

# This creates or opens the file 'user.db' as a database
conn = sqlite3.connect('banking.db') 
c = conn.cursor()

# Create user table/new bank account
c.execute("""CREATE TABLE IF NOT EXISTS registration 
            (id integer primary key, 
             full_name text, 
             age integer, 
             email text, 
             password text,
             address text,
             phone_number integer,
             account_type text,
             account_balance text)""")


#Create transaction table
c.execute("""CREATE TABLE IF NOT EXISTS transactions
            ( id integer primary key, 
             receiver_account_id integer, 
             transaction_type text,
             transaction_date text)""")

conn.commit()
conn.close()



#Function makes account for bank
def create_account(id, full_name, age, email, password, address, phone_number, 
                    account_type, account_balance):
    conn = sqlite3.connect('banking.db')
    c = conn.cursor()

    import random
    id = random.randint(1, 1000000)

    c.execute("""INSERT INTO registration  VALUES(?, ?, ?, ?, ?, ?, ?, ?)""", 
                (id,full_name, age, email, password, 
                address, phone_number, 
                account_type, account_balance))

    conn.commit()

    print(f"Account for {full_name} has been created! Your ID is {id}")
    conn.close()


#Function deletes bank account 
def delete_account(email, password):
  with sqlite3.connect('banking.db') as conn:
      c = conn.cursor()
      c.execute(""" DELETE FROM registration WHERE email = ? AND password = ?""",
                (email, password))
      conn.commit()
      print("Account has been deleted successfully!")




  #Function makes deposit from bank
def make_deposit(id, amount):
    conn = sqlite3.connect('banking.db')
    c = conn.cursor()

    c.execute("""UPDATE transactions SET account_balance = account_balance + ? 
              WHERE id = ?""",
              (amount, id))

    conn.commit()

    print("Deposit successful")
    conn.close()


  # Function makes withdraw from bank
def make_withdrawl(id, amount):
    conn = sqlite3.connect('banking.db')
    c = conn.cursor()

    c.execute("SELECT account_balance FROM transactions WHERE id = ?",
                (id, amount))
    #fetchone() returns a single record or none if no record found, link to what fetchone 
    #is (https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-  
    #fetchone.html)
    current_balance = c.fetchone()[0] 
    if current_balance >= amount:
      c.execute("""UPDATE registration SET account_balance = account_balance - ?
      WHERE id = ?"""
               , (id, amount))
      
      conn.commit()
      print("Withdrawl successful")
      conn.close()


  #Function checks balance of bank
def check_balance(id):
    conn = sqlite3.connect('banking.db')
    c = conn.cursor()
    c.execute("SELECT account_balance FROM registration WHERE id = ?",(id))
    account_balance = c.fetchone()[0]

    print(f"Your current balance is: {account_balance}")

    conn.close()

        
#Function Modifies Account Information
def modify_account(email, password, update):
  with sqlite3.connect('banking.db') as conn:
      c = conn.cursor()
      c.execute(f"""UPDATE registration SET {update} = ? WHERE email = ?AND password =
      ?""", (email, password, update))
      conn.commit()
      print("Account information updated successfully!")


#Checks the values in tables
def connect_database(database_name):
  conn = sqlite3.connect(database_name)
  return conn

def check_table_values(table_name):
  conn = connect_database('banking.db')
  c = conn.cursor()
  c.execute(f"SELECT * FROM {table_name}")
  rows = c.fetchall()
  if rows:
    print(f"Table {table_name} contains the following values:")
    for row in rows:
      print(row)
  else: 
    print(f"Table {table_name} is empty.")








  

  
  




  





