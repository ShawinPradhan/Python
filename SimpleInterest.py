
def simple_interest(principle,rate,time):
    return (principle * rate * time)/100

try:
    principle = float(input("Enter the principle: "))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time(year): "))

    print("Simple Interest: ", simple_interest(principle,rate,time))
    
except ValueError:
    print("Invalid input. Please enter valid value.")

##OUTPUT
##Enter the principle: 10000
##Enter the rate of interest: 8
##Enter the time(year): 2
##Simple Interest:  1600.0
