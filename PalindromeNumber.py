#Function to check whether a number is a palindrome number or not
def check_palindrome(num):
    original_num = num
    reverse = 0
    #Reversing a number using while loop
    while num>0:
        #Extracting the last_digit by finding the modules of the num by 10
        remainder = num%10

        #Adding the remainder into the variable reverse
        reverse = (reverse*10) + remainder

        #Removing the last_digit
        num = num//10

    if(original_num==reverse):
        return " is a Palindrome number"
    else:
        return " is not a Palindrome number"

num = int(input("Enter a number: "))

print(f"{num}",check_palindrome(num))

##OUTPUT
##Enter a number: 121
##121  is a Palindrome number
##
##Enter a number: 123
##123  is not a Palindrome number

