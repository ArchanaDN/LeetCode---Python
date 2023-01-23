# global variables
a = 10
b = 19

def add():
    c = a + b
    print(c)

add()

# non local variables
def fun1():
    var1 = 12
    def fun2():
        nonlocal var1
        var1 += 10
        print(var1)
    fun2()
fun1()

