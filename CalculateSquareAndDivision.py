#Function to divide two number
def div(dividend,divisor):
    return dividend/divisor

#Function to calculate the square of a number
def square(num):
    return pow(num,2)

while True:
    try:
        print("1) Division")
        print("2) Square of a number")
        print("3) Exit")

        choice = int(input("Enter the choice: "))
        if choice ==1:
            dividend = float(input("Enter the dividend: "))
            divisor = float(input("Enter the divisor: "))
            print(f"Quotient when {dividend}/{divisor} is: ",div(dividend,divisor))
        elif choice ==2:
            value = float(input("Enter the number: "))
            print(f"Square of {value}:", square(value))
        else:
            break
    except ValueError:
        print("Invalid Input!!")

'''
OUTPUT
1) Division
2) Square of a number
3) Exit
Enter the choice: 1
Enter the dividend: 20
Enter the divisor: 5
Quotient when 20.0/5.0 is:  4.0
1) Division
2) Square of a number
3) Exit
Enter the choice: 2
Enter the number: 9
Square of 9.0: 81.0
1) Division
2) Square of a number
3) Exit
Enter the choice: 3
'''  
