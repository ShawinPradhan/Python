#Function to convert kilometer to miles
def kilometer_to_miles(value):
    return value * 0.6214

#Function to convert miles to kilometer
def miles_to_kilometer(value):
    return value / 0.6214

#This loop will continue until we exit from the program
while True:
    try:
        print("Select the option below: ")
        print("1) Kilometer to miles")
        print("2) Miles to Kilometer")
        print("3) Exit")
       
        value = int(input("Enter the choice: "))
        
        if value==1:
            km = float(input("Enter the value in km: "))
            mile = round(kilometer_to_miles(km),2) #round off the value to 2 precision places
            print(f"{km} km is equal to {mile} miles")

        elif value ==2:
            mile = float(input("Enter the value in miles: "))
            km = round(miles_to_kilometer(mile),2)  #round off the value to 2 precision places
            print(f"{mile} miles is equal to {km} km")

        elif value ==3:
            break

        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter a valid value")

'''
OUTPUT
Select the option below: 
1) Kilometer to miles
2) Miles to Kilometer
3) Exit
Enter the choice: 1
Enter the value in km: 10
10.0 km is equal to 6.21 miles
Select the option below: 
1) Kilometer to miles
2) Miles to Kilometer
3) Exit
Enter the choice: 2
Enter the value in miles: 6.21
6.21 miles is equal to 9.99 km
Select the option below: 
1) Kilometer to miles
2) Miles to Kilometer
3) Exit
Enter the choice: 3
'''
