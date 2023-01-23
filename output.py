print("gdg \n trash")

# end attribute in print() function
print("fgt os dsgfjs", end = "***")
print()

#timer using flush
import time

seconds = 3
for i in reversed(range(seconds + 1)):
    if i > 0:
        print(i, end = ">>>", flush=True)
        time.sleep(1)
    else:
        print("start")

# Separator
# The print() function can accept any number of positional arguments. To separate these positional arguments , keyword argument “sep” is used.

a = 10
b = 9
c = 8
print(a, b, sep = '-')


#     print(a, b, sep = '-', c)
#                            ^
# SyntaxError: positional argument follows keyword argument

# file Argument
import io
dummy = io.StringIO()
print("Hello Hi", file = dummy)
dummy.getvalue()

print('Welcome to GFG : ', file = open('Testfile.txt', 'w')) 

l = [6, 6, 7, 4, 3]
print(*l)
print("vgh", end = " ") 
print("fhg")
import antigravity