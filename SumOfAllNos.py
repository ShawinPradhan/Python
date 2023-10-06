
#Variable to store the sum
total = 0

while True:
    num = int(input("Enter a number (Enter 0 to exit): "))

    #Checking if user wants to exit
    if num==0:
        break

    #Adding the number to total
    total += num;

print("Sum of all entered numbers: ",total)

 '''       
OUTPUT
Enter a number (Enter 0 to exit): 12
Enter a number (Enter 0 to exit): 13
Enter a number (Enter 0 to exit): 14
Enter a number (Enter 0 to exit): 15
Enter a number (Enter 0 to exit): 0
Sum of all entered numbers:  54
'''
