# tuples ---> ()

num= (1,2,3,4)
print(num, type(num))


# index 
stu_info= ("mohammad", True, 7.93, 22)
print(stu_info)
print(stu_info[0])
print(stu_info[0:3])
print(stu_info[-2])

name= ("Gamana,") * 3
print(name)
print(type(name))

# list constructor
list= [1,2,3]
print(list, type(list))
rgb = tuple(list)
print(rgb)
print(type(rgb))

# adding and removing elements
x= (1,2,3)
z= (10, 11, 12)
# z.pop()
del z

# loop
z= (10,11,12,10)
for i in range(len(z)):
    print(z[i])

# methods in touples
print(z.count(10))
print(z.index(10))
print(z.index(10,2))

# other methods
t = (10, 20, 30, 40, 50)

print(len(t))
print(max(t))
print(min(t))
print(sum(t))
print(sorted(t))
print(any(t))
print(all(t))
print(10 in t)

t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)
print(t1 * 2)

del t