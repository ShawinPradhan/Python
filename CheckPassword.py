
## List of valid passwords
valid_passwords = ['admin','user123']

#Function to check whether the password entered is valid or not
def valid_password(password):
    #checking if the password entered is present in list of valid passwords
    if password in valid_passwords:
        print("You have successfully logged in.")
    else:
        print("Please check the password!")

#taking input from the user
password = input("Please enter your password: ")
valid_password(password)

##OUTPUT
##Please enter your password: admin
##You have successfully logged in.
##
##Please enter your password: user123
##You have successfully logged in.
##
##Please enter your password: admin123
##Please check the password!
