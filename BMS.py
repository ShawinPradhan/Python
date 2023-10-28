import mysql.connector
from mysql.connector import IntegrityError  # Import IntegrityError
import random

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="banking_system"
)
cursor = conn.cursor()

# Create a table for account_type
cursor.execute("""
    CREATE TABLE IF NOT EXISTS account_type (
        acc_id INT AUTO_INCREMENT PRIMARY KEY,
        account_type VARCHAR(20) NOT NULL UNIQUE
    )
"""
)

# Create a table for accounts
cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        account_number VARCHAR(20) NOT NULL UNIQUE,
        first_name VARCHAR(30) NOT NULL,
        last_name VARCHAR(30) NOT NULL,
        balance DOUBLE(10, 2) NOT NULL,
        email VARCHAR(64) UNIQUE NOT NULL,
        aadhaar_no VARCHAR(12) UNIQUE NOT NULL,
        pan_card VARCHAR(10) UNIQUE NOT NULL,
        status VARCHAR(10) NOT NULL,
        acc_id int,
        foreign key(acc_id) references account_type(acc_id)
    )
"""
)
conn.commit()

#custom exception if account is not present in the system
class CustomerNotFound(Exception):
    def __init__(self, account_number):
        self.account_number = account_number
        super().__init__(f"Customer with account number {account_number} not found! Please contact the manager.")

#custom exception if account balance is insufficient balance
class InsufficientBalance(Exception):
    def __init__(self, balance):
        self.balance = balance
        super().__init__(f"Account balance is insufficient! Current balance: {balance}")

#function to create account
def create_account(first_name, last_name, initial_balance, email, aadhaar_no, pan_card):
        # Generate a unique account number
        bank_name = "HDFC"
        # account_number = f"{bank_name}{hash(bank_name) % 10000}"
        number = ''.join(str(random.randint(0, 9)) for _ in range(5))
        account_number = bank_name+number
        
        print("What type of account you want to create?")
        accType =int(input("Enter: 1) Savings A/C,  2) Current A/C:  "))
        if accType==1:
            try:
                # Insert a new account into the database
                cursor.execute("""
                    INSERT INTO accounts (account_number, first_name, last_name, balance,
                    email, aadhaar_no, pan_card, status, acc_id)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (account_number, first_name, last_name, initial_balance, email, aadhaar_no, pan_card, "ACTIVE", 1))
                conn.commit()
                print(f"Account created successfully. Your account number is: {account_number}")

            except IntegrityError as e:
                print(f"Error: {e}")
                print("Account already present!")

            except Exception as e:
                print(f"Error: {e}")
                print("An error occurred while creating the account.")

        elif accType==2:
            try:
                # Insert a new account into the database
                cursor.execute("""
                    INSERT INTO accounts (account_number, first_name, last_name, balance,
                    email, aadhaar_no, pan_card, status, acc_id)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (account_number, first_name, last_name, initial_balance, email, aadhaar_no, pan_card,"ACTIVE", 2))
                conn.commit()
                print(f"Account created successfully. Your account number is: {account_number}")

            except IntegrityError as e:
                print(f"Error: {e}")
                print("Account already present!")

            except Exception as e:
                print(f"Error: {e}")
                print("An error occurred while creating the account.")

        else:
            print("Wrong Choice!!")

   

#function to deposit amount into the account
def deposit(account_number):
    cursor.execute("""
        SELECT *
        FROM accountS
        WHERE account_number = %s and status = 'ACTIVE'
    """, (account_number,))
    account = cursor.fetchone()
    if account:
        amount = float(input("Enter deposit amount: "))
        # Update the balance by depositing money into the account
        cursor.execute("""
            UPDATE accounts
            SET balance = balance + %s
            WHERE account_number = %s
        """, (amount, account_number))
        conn.commit()
        print("Deposit successful!")
        
        # Retrieve and display the updated account balance
        cursor.execute("SELECT balance FROM accounts WHERE account_number = %s", (account_number,))
        balance = cursor.fetchone()[0]
        print(f"Updated account balance: Rs.{balance:.2f}")

    else:
        raise CustomerNotFound(account_number) 

    

#function to withdraw amount from the account
def withdraw(account_number):
    cursor.execute("""
        SELECT *
        FROM accountS
        WHERE account_number = %s and status = 'ACTIVE'
    """, (account_number,))
    account = cursor.fetchone()
    if account:
        amount = float(input("Enter withdrawal amount: "))
        # Check if there's enough balance before withdrawing
        cursor.execute("SELECT balance FROM accounts WHERE account_number = %s", (account_number,))
        balance = cursor.fetchone()[0]
        if balance >= amount:
            cursor.execute("""
                UPDATE accounts
                SET balance = balance - %s
                WHERE account_number = %s
            """, (amount, account_number))
            conn.commit()
            print("Withdrawal successful!")
            
            # Retrieve and display the updated account balance
            cursor.execute("SELECT balance FROM accounts WHERE account_number = %s", (account_number,))
            balance = cursor.fetchone()[0]
            print(f"Updated account balance: Rs.{balance:.2f}")
            
        else:
            # Retrieve and display the current account balance
            cursor.execute("SELECT balance FROM accounts WHERE account_number = %s", (account_number,))
            balance = cursor.fetchone()[0]
            raise InsufficientBalance(balance)

    else:
        raise CustomerNotFound(account_number)

    

#function to display account balance
def display_balance(account_number):
    cursor.execute("""
        SELECT *
        FROM accountS
        WHERE account_number = %s and status = 'ACTIVE'
    """, (account_number,))
    account = cursor.fetchone()
    if account:
        # Retrieve and display the account balance
        cursor.execute("SELECT balance FROM accounts WHERE account_number = %s", (account_number,))
        balance = cursor.fetchone()[0]
        print(f"Account balance: Rs.{balance:.2f}")

    else:
        raise CustomerNotFound(account_number)

# function to display account details
def account_details(account_number):
    # Retrieve all the details from the database of a customer
    cursor.execute("""
        SELECT a.account_number, a.first_name, a.last_name, a.balance, a.email, a.aadhaar_no, a.pan_card, at.account_type
        FROM accounts a
        JOIN account_type at ON a.acc_id = at.acc_id
        WHERE a.account_number = %s and status = 'ACTIVE'
    """, (account_number,))
    account = cursor.fetchone()
    
    if account:
        account_number, first_name, last_name, balance, email, aadhaar_no, pan_card, account_type = account
        print("Account Details:")
        print(f"Account Number: {account_number}")
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Balance: Rs.{balance:.2f}")
        print(f"Email: {email}")
        print(f"Aadhaar Number: {aadhaar_no}")
        print(f"PAN Card: {pan_card}")
        print(f"Account Type: {account_type}")
    else:
        raise CustomerNotFound(account_number)

#function to close the account
def close_account(account_number):
    cursor.execute("""
        SELECT *
        FROM accounts
        WHERE account_number = %s and status = 'ACTIVE'
    """, (account_number,))
    account = cursor.fetchone()
    if account:
        cursor.execute("""
                UPDATE accounts
                SET status = 'INACTIVE'
                WHERE account_number = %s
            """, (account_number,))
        conn.commit()
        print("Account has been closed!")

    else:
        raise CustomerNotFound(account_number)
        

# Main program
while True:
    print("\nBanking Management System")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Account details")
    print("6. Close Account")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            first_name = input("Enter account holder's first name: ")
            last_name = input("Enter account holder's last name: ")
            initial_balance = float(input("Enter initial balance: "))
            email = str(input("Enter email address: "))
            aadhaar = int(input("Enter aadhaar no.: "))
            pan = str(input("Enter pan card no.: "))
            create_account(first_name, last_name, initial_balance, email, aadhaar, pan)
            
        except ValueError:
            print("Invalid Input!! Please enter valid details.")

            
    elif choice == "2":
        try:
            account_number = input("Enter account number: ")
            deposit(account_number)
            
        except ValueError:
            print("Invalid Input!! Please enter valid details.")

        except CustomerNotFound as e:
            print(e)
        
    elif choice == "3":
        try:
            account_number = input("Enter account number: ")
            withdraw(account_number)
            
        except ValueError:
            print("Invalid Input!! Please enter valid details.")

        except CustomerNotFound as e:
            print(e)

        except InsufficientBalance as e:
            print(e)
        
    elif choice == "4":
        try:
            account_number = input("Enter account number: ")
            display_balance(account_number)
            
        except ValueError:
            print("Invalid Input!! Please enter valid details.")

        except CustomerNotFound as e:
            print(e)

    elif choice == "5":
        try:
            account_number = input("Enter account number: ")
            account_details(account_number)
            
        except ValueError:
            print("Invalid Input!! Please enter a valid account number.")
            
        except CustomerNotFound as e:
            print(e)

    elif choice == "6":
        try:
            account_number = input("Enter account number: ")
            close_account(account_number)
            
        except ValueError:
            print("Invalid Input!! Please enter a valid account number.")
            
        except CustomerNotFound as e:
            print(e)
            
    
    elif choice == "7":
        print("Exiting the program. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")

# Close the database connection
conn.close()


'''
OUTPUT:

Banking Management System
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Account details
6. Close Account
7. Exit
Enter your choice: 1
Enter account holder's first name: Dipankar
Enter account holder's last name: Das
Enter initial balance: 50000
Enter email address: dip@gmail.com
Enter aadhaar no.: 564123456789
Enter pan card no.: EJFP456210
What type of account you want to create?
Enter: 1) Savings A/C,  2) Current A/C:  1
Account created successfully. Your account number is: HDFC2282

Banking Management System
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Account details
6. Close Account
7. Exit
Enter your choice: 1
Enter account holder's first name: Dip
Enter account holder's last name: Das
Enter initial balance: 5000
Enter email address: dip@gmail.com
Enter aadhaar no.: 456123457893
Enter pan card no.: EJFK124569
What type of account you want to create?
Enter: 1) Savings A/C,  2) Current A/C:  1
Error: 1062 (23000): Duplicate entry 'dip@gmail.com' for key 'accounts.email'
Account already present!

Banking Management System
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Account details
6. Close Account
7. Exit
Enter your choice: HDFC2282
Invalid choice. Please try again.

Banking Management System
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Account details
6. Close Account
7. Exit
Enter your choice: 2
Enter account number: HDFC2282
Enter deposit amount: 5000
Deposit successful!
Updated account balance: Rs.55000.00

Banking Management System
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Account details
6. Close Account
7. Exit
Enter your choice: 4
Enter account number: HDFC2282
Account balance: Rs.55000.00

Banking Management System
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Account details
6. Close Account
7. Exit
Enter your choice: 3
Enter account number: HDFC2282
Enter withdrawal amount: 60000
Account balance is insufficient! Current balance: 55000.0

Banking Management System
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Account details
6. Close Account
7. Exit
Enter your choice: 3
Enter account number: HDFC2282
Enter withdrawal amount: 4000
Withdrawal successful!
Updated account balance: Rs.51000.00

Banking Management System
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Account details
6. Close Account
7. Exit
Enter your choice: 5
Enter account number: HDFC2282
Account Details:
Account Number: HDFC2282
First Name: Dipankar
Last Name: Das
Balance: Rs.51000.00
Email: dip@gmail.com
Aadhaar Number: 564123456789
PAN Card: EJFP456210
Account Type: Savings

Banking Management System
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Account details
6. Close Account
7. Exit
Enter your choice: 6
Enter account number: HDFC2282
Account has been closed!

Banking Management System
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Account details
6. Close Account
7. Exit
Enter your choice: 2
Enter account number: HDFC2282
Customer with account number HDFC2282 not found! Please contact the manager.

Banking Management System
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Account details
6. Close Account
7. Exit
Enter your choice: 7
Exiting the program. Goodbye!


'''
