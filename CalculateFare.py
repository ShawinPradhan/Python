
def calculate_charge(distance):
    if distance in range(1,50):
        return distance * 8
    elif distance in range(51,100):
        return distance * 10
    else:
        return distance * 12

distance = int(input("Enter the distance to calculate the fare: "))
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
