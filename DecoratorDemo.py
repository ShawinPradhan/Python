'''
In Python, decorators are a powerful and flexible
way to modify or enhance the behavior of functions or
methods without changing their source code.
Decorators allow you to add functionality to functions
dynamically. They are often used for tasks such as
logging, authentication, and performance measurement.

A decorator is a function that takes another function
as its argument and returns a new function that usually
extends or modifies the behavior of the original
function. Decorators are typically applied using the
"@" symbol just before the function definition.
'''
from datetime import datetime as dt

#here in main function we are passing a parameter f
#f is calling our other function where decorator is defined
#since python uses interpreter the first function it
#reaches it gets executed first
def main(f):
    start = dt.now()
    f()
    end = dt.now()

    print("Total time taken:",(end-start))

#the annotation will be same as the original function
@main
def even():
    print("Even numbers")
    for i in range (1,100,1):
        if i%2==0:
            print(i)
@main
def odd():
    print("Odd numbers")
    for i in range (1,100,1):
        if i%2!=0:
            print(i)

