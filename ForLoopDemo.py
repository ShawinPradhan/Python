#program for if loop
age = 25 #declaring the variables
weight = 65
gender ='Male'
if age>=25 and weight>=55 and gender=='Male':
	print("Yes, you can donate blood")
else:
	print("No, you cannot donate blood")

#another way
#if multiple conditions are present then put it
#inside the list.
age = 25 #declaring the variables
weight = 65
gender ='Male'
con = [age>=25,weight>=55, gender=='Male']
# all - is used to check whether all conditions are matched
# any - is used to check any one of the conditions
# if any(con):
if all(con):
	print("Yes, you can donate blood")
else:
	print("No, you cannot donate blood")