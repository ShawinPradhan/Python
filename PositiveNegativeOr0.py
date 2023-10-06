def check_number(num):
    if num>0:
        return "Positive Number"
    elif num<0:
        return "Negative Number"
    else:
        return "0"
        

num = int(input("Enter a number: "))
print(f"{num} is a ",check_number(num))

'''
OUTPUT
Enter a number: 23
23 is a  Positive Number
Enter a number: -5
-5 is a  Negative Number
Enter a number: 0
0 is a  0
'''
