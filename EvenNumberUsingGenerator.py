#if we use square brackets then the type is going to be list
#even = [i for i in range(10) if i%2==0]

#by using comman brackets the type changes to generator
even = (i for i in range(10) if i%2==0)
print(type(even))
#print(next(even))

for i in even:
    print(i)
