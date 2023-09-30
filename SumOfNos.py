# Initialize a variable to store the sum
total_sum = 0;

print("Enter 5 integer values:")
# Loop to get input for 5 numbers
for i in range(5):
    try:
        # Get user input as a number and add it to the total
        num = int(input())
        total_sum += num;
    except ValueError:
        print("Invalid input! Please enter a valid number")

print(f"The sum of the 5 numbers is: {total_sum}")

##OUTPUT:
##Enter 5 integer values:
##1
##2
##3
##4
##5
##The sum of the 5 numbers is: 15
