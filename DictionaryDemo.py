##Dictionary - Data Structure
##It will store the data in key and value pair.
##The key should be unique.
##If we take the same key the last added value with the key
##is going to replace the first value that was the added using
##the same key.
##Dictionary is mostly used for unstructured data or for
##JSON format.
data={'name':'Shawin','age':25,'sal':2500}

##to print all the keys present in the dictionary
print(data.keys())

##to print all the values present in the dictionary
print(data.values())




##we can add multiple values to the same key by passing list
data={'name':['Shawin','Raj'],'age':[25,30],'sal':[4000,2500]}

##to print both the keys and values in the dictionary
##items consist of key and value here in i key is stored
##where as in j value is stored
for i,j in data.items():
	print(i,j);
