age = input("Whats your age? ")
data_type = type(age)
print(data_type)

age = int(age)
data_type = type(age)
print(data_type)

print("Your age in dog year: ", age * 7)

grocery = ['apple', 'orange', 'banana']

grocery = tuple(grocery)

print(grocery)
print(type(grocery))
