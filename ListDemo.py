# List Slicing:
# Any data can be added to the list like string, floating number,
# whole number, etc.
# It is mutable, the order of iteration is also maintained.
#
# append - To add new element to the list
# e.g list.append(value)
#
# pop - to remove the element from the list by passing the index
# e.g list.pop(2)
# if passed without parameter will always pop the last element
#
# remove - to remove the element from the list by passing
# which object we want to remove
# e.g. list.remove('Sachin')
#
# copy - to copy the whole members from one list to another
# e.g. list2 = list.copy()
#
# when we do list=list2, we are actually assigning the same
# location so if any new data added in list2 will be seen in
# list as well but does not work with copy method.
#
# clear - to remove all the values present in the list
# e.g. list.clear()
#
# insert - to insert a new element in between the list
# e.g. list.insert(index, object) -> list.insert(2,'Anudip')
#
# To change the value in the list
# list[index] = object
# e.g. list[2] = 5
#
# To delete a range of values from the list
# del list[0:3]
# Here values present in index 0,1,2 are going to be deleted

#Program to take value from the user in a list
data=[]  #empty list
x = input("Enter a value:")
data.append(x) #adding the value into list
print(data) #printing the list

data=[]  #empty list
x = eval(input("Enter a value:"))
#eval - is going to evaluate the type of data that the user has entered
#eval can only evaluate int or floating numbers, if
#string is passed it will throw error
data.append(x) #adding the value into list
print(type(data[0])) #printing the list


#Program to take multiple values from the user
data1 = []
#for i in [1,2,3,4,5]:

#range takes 3 parameters, one is mandatory other two is not
#range(start value, end value, increment value)
#end value is mandatory
for i in range(5):
 y = int(input("Enter a value:"))
 data1.append(y)
print(data1)

