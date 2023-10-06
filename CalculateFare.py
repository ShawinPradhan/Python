#function to calculate the fare according to the distance
def calculate_charge(distance):
    #if the distance is between 1 to 50 then the user will be charged 8 Rs./km
    if distance in range(1,50):
        return distance * 8
    #if the distance is between 51 to 100 then the user will be charged 10 Rs./km
    elif distance in range(51,100):
        return distance * 10
     #else if the distance greater than 100 then the user will be charged 12 Rs./km
    else:
        return distance * 12

#Taking the distance as input from the user
distance = int(input("Enter the distance to calculate the fare: "))

#Checking if the distance is a positive number
if(distance>0):
    print(f"Fare: Rs. ",calculate_charge(distance))
else:
    print("Distance should be greater than 0.")

'''
OUTPUT
Enter the distance to calculate the fare: 10
Fare: Rs. 80

Enter the distance to calculate the fare: 100
Fare: Rs. 1200

Enter the distance to calculate the fare: 120
Fare: Rs. 1440

Enter the distance to calculate the fare: 0
Distance should be greater than 0.
'''
