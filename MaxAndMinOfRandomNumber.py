import random

#Function to generate randome 5 number from 1 to 50
def generate_random_number():
    return [random.randint(1,50) for i in range(5)]

#Printing the random numbers
random = generate_random_number()
print("Random Numbers: ",random)

#Finding the maximum number using max() function
print("Maximum Number: ",max(random))

#Finding the minimum number using min() function
print("Minimum Number: ",min(random))


##OUTPUT
##Random Numbers:  [34, 17, 2, 20, 37]
##Maximum Number:  37
##Minimum Number:  2
