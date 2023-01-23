# multiple inputs
a, b = input("Enter two values : ").split(",")
print(a)
print(b)

#a, b = input("Enter two values : ").split(",")
print("The first value is {} and the second value is {}".format(a,b))

#Getting a list as input
x = list(map(int, input("Enter list of numbers : ").split()))
print(x)

#Taking multiple imputs at a time
x = [int(x) for x in input("Enter the list of values").split()]
print(x)