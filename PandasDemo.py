import pandas as pd

data = {"Roll":[1,None,3],"Name":["John",None,"Jack"],\
        "Age":[27,25,29]}
df = pd.DataFrame(data)

print(df)
##   Roll   Name  Age
##0     1   John   27
##1     2  Smith   25
##2     3   Jack   29

print(df['Age']>27)
##0    False
##1    False
##2     True
##Name: Age, dtype: bool

#to print only true values - slicing
print(df[df['Age']>27])
##   Roll  Name  Age
##2     3  Jack   29

#to store the data into a csv file
#df.to_csv("Data.csv",index=False)

print(df.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   Roll    3 non-null      int64 
 1   Name    2 non-null      object
 2   Age     3 non-null      int64 
dtypes: int64(2), object(1)
memory usage: 204.0+ bytes
None  '''

#to check the dimension of the dataframe
print(df.shape)
#(3, 3)

#to check how many null values are there in df
print(df.isna().sum())
##Roll    0
##Name    1
##Age     0
##dtype: int64

print(df)
##   Roll  Name  Age
##0     1  John   27
##1     2  None   25
##2     3  Jack   29

#df.dropna(inplace=True) #it will completely remove the data#
#print(df)
##   Roll  Name  Age
##0     1  John   27
##2     3  Jack   29

#it will replace all the null values with NA
#df.fillna("NA",inplace=True)

#so to be more specific we pass along the column name
df['Name'].fillna("NA",inplace=True)
print(df)
##   Roll  Name  Age
##0     1  John   27
##1     2    NA   25
##2     3  Jack   29

df['Roll'].fillna(df['Roll'].median(),inplace=True)
print(df)
##   Roll  Name  Age
##0   1.0  John   27
##1   2.0    NA   25
##2   3.0  Jack   29


#it will drop all the duplicate values
#df.drop_duplicates(inplace=True)

print(df['Age'].describe())
##count     3.0
##mean     27.0
##std       2.0
##min      25.0
##25%      26.0
##50%      27.0
##75%      28.0
##max      29.0
##Name: Age, dtype: float64

#describe will be used to stastical purpose
#it will only work with numerical columns
print(df.describe())
##       Roll   Age
##count   3.0   3.0
##mean    2.0  27.0
##std     1.0   2.0
##min     1.0  25.0
##25%     1.5  26.0
##50%     2.0  27.0
##75%     2.5  28.0
##max     3.0  29.0

#to add one new columns to the dataFrame
address = ['Kolkata','Delhi','Goa']
df['Address']=address
#another way
#df.assign(address = ['Kolkata','Delhi','Goa'])
print(df)
##   Roll  Name  Age  Address
##0   1.0  John   27  Kolkata
##1   2.0    NA   25    Delhi
##2   3.0  Jack   29      Goa

#to add a new row to the DataFrame
#new_row = {"Roll":4,"Name:":'Rahul',"Age":28,"Address":"Darjeeling"}
#df._append(new_row,ignore_index=True) #this is not working
df.loc[len(df.index)]=[4,'Rahul',28,'Darjeeling']
print(df)
##   Roll   Name  Age     Address
##0   1.0   John   27     Kolkata
##1   2.0     NA   25       Delhi
##2   3.0   Jack   29         Goa
##3   4.0  Rahul   28  Darjeeling




