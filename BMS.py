import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="banking_system"
)
cursor = conn.cursor()

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
        pan_card VARCHAR(10) UNIQUE NOT NULL
    )
"""
)
conn.commit()

#function to create account
def create_account(first_name, last_name, initial_balance, email, aadhaar_no, pan_card):
    # Generate a unique account number (you can implement this differently)
    bank_name = "HDFC"
    account_number = f"{bank_name}{hash(bank_name) % 10000}"
    # Insert a new account into the database
    cursor.execute("""
        INSERT INTO accounts (account_number, first_name, last_name, balance, email, aadhaar_no, pan_card)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (account_number, first_name, last_name, initial_balance, email, aadhaar_no, pan_card))
    conn.commit()
    print(f"Account created successfully. Your account number is: {account_number}")

#function to deposit amount into the account
def deposit(account_number, amount):
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

#function to withdraw amount from the account
def withdraw(account_number, amount):
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
    else:
        print("Insufficient balance!")

    # Retrieve and display the updated account balance
    cursor.execute("SELECT balance FROM accounts WHERE account_number = %s", (account_number,))
    balance = cursor.fetchone()[0]
    print(f"Updated account balance: Rs.{balance:.2f}")

#function to display account balance
def display_balance(account_number):
    # Retrieve and display the account balance
    cursor.execute("SELECT balance FROM accounts WHERE account_number = %s", (account_number,))
    balance = cursor.fetchone()[0]
    print(f"Account balance: Rs.{balance:.2f}")

# function to display account details
def account_details(account_number):
    # Retrieve all the details from the database
    cursor.execute("""
        SELECT account_number, first_name, last_name, balance, email, aadhaar_no, pan_card
        FROM accounts
        WHERE account_number = %s
    """, (account_number,))
    account = cursor.fetchone()
    if account:
        account_number, first_name, last_name, balance, email, aadhaar_no, pan_card = account
        print("Account Details:")
        print(f"Account Number: {account_number}")
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Balance: Rs.{balance:.2f}")
        print(f"Email: {email}")
        print(f"Aadhaar Number: {aadhaar_no}")
        print(f"PAN Card: {pan_card}")
    else:
        print("Account not found.")

# Main program
while True:
    print("\nBanking Management System")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Account details")
    print("6. Exit")

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
            amount = float(input("Enter deposit amount: "))
            deposit(account_number, amount)
            
        except ValueError:
            print("Invalid Input!! Please enter valid details.")
        
    elif choice == "3":
        try:
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            withdraw(account_number, amount)
            
        except ValueError:
            print("Invalid Input!! Please enter valid details.")
        
    elif choice == "4":
        try:
            account_number = input("Enter account number: ")
            display_balance(account_number)
            
        except ValueError:
            print("Invalid Input!! Please enter valid details.")

    elif choice == "5":
        try:
            account_number = input("Enter account number: ")
            account_details(account_number)
        except ValueError:
            print("Invalid Input!! Please enter a valid account number.")
        
    elif choice == "6":
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
6. Exit
Enter your choice: 1
Enter account holder's first name: John
Enter account holder's last name: Doe
Enter initial balance: 25000
Enter email address: john@gmail.com
Enter aadhaar no.: 568947125360
Enter pan card no.: EJFL564892
Account created successfully. Your account number is: HDFC4211

Banking Management System
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Account details
6. Exit
Enter your choice: 2
Enter account number: HDFC4211
Enter deposit amount: 5000
Deposit successful!
Updated account balance: Rs.30000.00

Banking Management System
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Account details
6. Exit
Enter your choice: 3
Enter account number: HDFC4211
Enter withdrawal amount: 3000
Withdrawal successful!
Updated account balance: Rs.27000.00

Banking Management System
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Account details
6. Exit
Enter your choice: 4
Enter account number: HDFC4211
Account balance: Rs.27000.00

Banking Management System
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Account details
6. Exit
Enter your choice: 5
Enter account number: HDFC4211
Account Details:
Account Number: HDFC4211
First Name: John
Last Name: Doe
Balance: Rs.27000.00
Email: john@gmail.com
Aadhaar Number: 568947125360
PAN Card: EJFL564892

Banking Management System
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Account details
6. Exit
Enter your choice: 7
Invalid choice. Please try again.

Banking Management System
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Account details
6. Exit
Enter your choice: 2
Enter account number: HDFC4211
Enter deposit amount: as
Invalid Input!! Please enter valid details.

Banking Management System
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Account details
6. Exit
Enter your choice: 6
Exiting the program. Goodbye!


'''
