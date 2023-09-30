##Tuples:
##
##Tuples are immutable meaning new values cannot be added.
##It is much faster than the list for iterating over the elements.

data = 11,22,55,66,78,88
print(type(data))
#<class 'tuple'>
print(data[5]) #fetches the data present in index 5
print(data[0:5]) #fetces the data from index 0 to 5-1
#data[0] = 5 #this is not supported as tuple is immutable
#data.append(55) #not supported

##data = (55)
##type(data) #int
##
##data(55,)
##type(data) #tuple


#we can also added list inside a tuple
data =(1,2,3,4,5,[5,6,7,8],5,6)
print(type(data)) #tuple

##In the above list present inside the tuple we can add new
##data where in the tuple we cannot
data[5].append(99)
#data --> (1,2,3,4,5,[5,6,7,8,99],5,6)

##We can also have nested tuple also
data = ((1,2,3),(4,5,6),(7,8,9))
print(len(data)) #3
print(data[0]) #(1,2,3)
