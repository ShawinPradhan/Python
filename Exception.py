a = 20
b = 0

print(a+b)
#here same as in java we use the try block where we write the codes where exception might occur
try:
    print(a/b)
#instead of catch we use except to handle the exception
#if we pass the exception along with except keyword then it is going to just handle that exception
#except: this will handle all the exceptions
except ZeroDivisionError:
    print("Unable to divide")
#else statement is used to execute if no exception occurs
#it is ignored if exception occurs
else:
    print("No exception occured")
#finally block is used to deallocate the resources
finally:
    print("This is finally block")
