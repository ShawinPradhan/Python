#SET data-structure
##It is by default sorted and only unique values can be 
##stored. No duplicate values are allowed.
##Only numerical values are sorted but does not work for string.
##Inside set we cannot added list type.
##We can add tuples in the set.
##Order of insertion is also not maintained.


##If a question is asked to only print the unique values
##from a list and print it we can convert it to set and print it
data = [5,6,9,8,8,1,2]
data2 = set(data)
print(data2)
#data2 --> {1,2,5,6,8,9}

#add - method to add element in a set
data2.add(10)
print(data2)  # {1,2,5,6,8,9,10}

##Problem- To show only the unique values from the csv file
##To read data from a csv file we use the pandas
##import pandas as pd
##
##x = pd.read_csv('std.csv')
##u = set(x['Name'])  #Name - column name
##print(u)
