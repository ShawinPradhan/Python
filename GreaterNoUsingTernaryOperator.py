def greaterNo(num1,num2):
    return num1 if num1>num2 else num2


num1 = float(input("Enter the first digit: "))
num2 = float(input("Enter the second digit: "))

print("Greater number is: ",greaterNo(num1,num2))

##OUTPUT
##Enter the first digit: 23
##Enter the second digit: 12
##Greater number is:  23.0
