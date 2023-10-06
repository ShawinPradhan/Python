
num = int(input("Enter a number: "))

reverse = 0

#Reversing a number using while loop
while num>0:
    #Extracting the last_digit by finding the modules of the num by 10
    remainder = num%10

    #Adding the remainder into the variable reverse
    reverse = (reverse*10) + remainder

    #Removing the last_digit
    num = num//10

#Printing the reversed number
print("Reversed Number: ",reverse)

##OUTPUT
##Enter a number: 567
##Reversed Number:  765
