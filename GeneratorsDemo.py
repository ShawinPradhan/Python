#using generators it is going to take less time to execute
'''
Generators are a powerful and memory-efficient way to
create iterators in Python. They allow you to iterate
over a potentially large sequence of data without storing
it all in memory at once. Instead of generating and
storing all the values in advance, generators produce
values on-the-fly as you iterate over them.
This can be particularly useful when dealing with large
datasets or when you want to create an iterable from a
dynamic data source.'''

from datetime import datetime as dt

#without using generators
print("Without using generators")
start_time = dt.now() #it will fetch the current time

for i in range(1,10,1):
    print(i)
    
end_time = dt.now()

print("Total Time Taken:",(end_time-start_time))

print()

#using generators
print("Using generators")
start_time = dt.now() #it will fetch the current time

def loop():
    for i in range(1,10,1):
        yield i
    
end_time = dt.now()
x=loop()
#print(next(x)) #it will only print one value
for i in x:
    print(i)

print("Total Time Taken:",(end_time-start_time))

'''
OUTPUT
Without using generators
1
2
3
4
5
6
7
8
9
Total Time Taken: 0:00:00.050266

Using generators
1
2
3
4
5
6
7
8
9
Total Time Taken: 0:00:00  '''


