#Program to print even numbers in a given range

#function to check whether a num is an even num or not
def isEven(num):
    if num%2 != 0:
        print(num)

#taking input from the user for starting and end range
start = int(input("Enter the start of range:"))
end = int(input("Enter the end of range:"))

#iterating over each number from start to end
for num in range(start,end+1):
    isEven(num)

##OUTPUT
##Enter the start of range:1
##Enter the end of range:11
##1
##3
##5
##7
##9
##11
        
