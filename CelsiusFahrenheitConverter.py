

while True:
    try:
        print("Select the option below: ")
        print("1) Celsius to Farenheit")
        print("2) Farenheit to Celsius")
        print("3) Exit")
       
        value = int(input("Enter the choice: "))
        
        if value==1:
            celsius = float(input("Enter celsius degree: "))
            fahrenheit = celsius * 9/5 + 32
            print(f"{celsius}°C is equal to {fahrenheit}°F")

        elif value ==2:
            fahrenheit = float(input("Enter fahrenheit degree: "))
            celsius = (fahrenheit-32) * 5/9
            print(f"{fahrenheit}°F is equal to {celsius}°C")

        elif value ==3:
            break

        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter a valid value")

'''
OUTPUT
Select the option below: 
1) Celsius to Farenheit
2) Farenheit to Celsius
3) Exit
Enter the choice: 1
Enter celsius degree: 32
32.0°C is equal to 89.6°F
Select the option below: 
1) Celsius to Farenheit
2) Farenheit to Celsius
3) Exit
Enter the choice: 2
Enter fahrenheit degree: 89.6
89.6°F is equal to 32.0°C
Select the option below: 
1) Celsius to Farenheit
2) Farenheit to Celsius
3) Exit
Enter the choice: 3
'''

        

        
