#open(file name with the location, access mode)
#since file is not found it throw an exception called FileNotFoundError

#r - read mode
#w - write mode
#a - append mode
# try:
#      x = open("E:\Python\Data.txt","a")
#      print(x)
#      x.write("This is a text file")
#      # write functions always uses str so we pass a number it will show an error
#      x.write("\n") #new line
#      x.write(str(30))
#      print("File created successfully")
#      x.close()
# except FileNotFoundError:
#     print("File is not found")


# try:
#      x = open("E:\Python\Data.txt","r")
#      #print(x.read())
#      #readlines() - will store the data in list format
#      print(x.readlines())
#      x.close()
#      #to check if x is closed or not
#      print(x.closed) #it will return True as we have closed the file
# except FileNotFoundError:
#     print("File is not found")

#auto-close function in python
#using with it will make sure to close the file
try:
     with open("E:\Python\Data.txt","r") as x:
         print(x.read())
except FileNotFoundError:
    print("File is not found")
print(x.closed)