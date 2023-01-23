a = 4
b = 0

try:
    k = a//b
    print(k)

except ZeroDivisionError:
    print("Exception")

finally:
    print("In finally block")

print("a/b is : ")
assert b != 0, "b is 0 so divide by 0 error"
# print(a/b)