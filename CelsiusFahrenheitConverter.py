#Program to convert Celsius to Fahrenheit and vice versa

while True:
    try:
        print("Select the option below: ")
        print("1) Celsius to Farenheit")
        print("2) Farenheit to Celsius")
        print("3) Exit")
       
        choice = int(input("Enter the choice: "))

        #if choice is 1 then we are converting from celsius to fahrenheit
        if choice==1:
            celsius = float(input("Enter celsius degree: "))
            fahrenheit = celsius * 9/5 + 32
            print(f"{celsius}°C is equal to {fahrenheit}°F")

        #if choice is 2 then we are converting from fahrenheit to celsius
        elif choice ==2:
            fahrenheit = float(input("Enter fahrenheit degree: "))
            celsius = (fahrenheit-32) * 5/9
            print(f"{fahrenheit}°F is equal to {celsius}°C")

        #if choice is 3 then breaking out of the loop
        elif choice ==3:
            break

        else:
            print("Invalid choice")

    #handling the exception ValueError
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

        

        
