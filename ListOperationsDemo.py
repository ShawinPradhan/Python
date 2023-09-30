#program to find the max, min, sum, len of values in a list
#also how to sort data using sorted
data=[4,5,67,56,98,12]
print(max(data))  #prints the max value
print(min(data))  #prints the min value
print(sum(data))  #prints the sum value
len(data) #gives the length of the list

#to sorted the data in ascending order
sort = sorted(data)
print(sort)

#sort in descending order
desc = sorted(data, reverse=True)
print(desc)
