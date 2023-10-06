#Taking the input from the user
num = int(input("Enter a number: "))

#Checking if number is a positive number
if(num>0):
    original_num = num
    factorial = 1
    i = 1

    #this loop will continue till i is less than or equal to the number
    while i<=num:
        factorial *= i #factorial = factorial * i
        i += 1 #incrementing the value of i by 1

    print(f"Factorial of {original_num}:",factorial)
    
else:
    print("Please enter a positive number")


##OUTPUT
##Enter a number: 5
##Factorial of 5: 120
