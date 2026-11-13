# find large num:
def largest():
    a=10
    b=20
    c=30
    if a>b and a>c:
        print("a is big")
    elif b>a and b>c:
        print("b is big")
    else:
        print("c is big")
largest()


# no input & no output:
def square ():
    n=5*5
    print(n)
print (square())

# no input & output:
def square():
    n=5*5
    return n
print(square()) 

# input & no output:
def square(n):
    res=n*n
    print(res)
square(10)

# input & output:
def square(n):
    return n*n
res=square(10)   
print(res)

