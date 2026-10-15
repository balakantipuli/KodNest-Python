name="bala"
age=22
print(name)
print(id(name))

print("Hello Python",end=" - ")
print("Thankyou Python")

print("Hello Python \nThankyou Python")
# My name is bala and age is 22 str + str
# Option 1: Using commas (separates arguments, adds space automatically)
print("my name is", name, "and my age is", age)

# Option 2: Using string concatenation with +
print("my name is " + name + " and my age is " + str(age))

# f - strings
print(f"my name is {name} and my age is {age}")
