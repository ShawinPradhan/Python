
#method to check whether a number is an even or odd number
def even_odd(num):
    result = "is an Even Number" if num%2==0 else "is an Odd Number"
    return result

try:
    number = int(input("Enter a number: "))
    result = even_odd(number)
    print(number, result)
#if the user enters invalid character other than numeric value
#ValueError exception will be thrown thus we are handling it
#to print a meaningful message
except ValueError:
    print("Please enter valid number")

''' multi-line comment
OUTPUT
Enter a number: 5
5 is an Odd Number
'''
