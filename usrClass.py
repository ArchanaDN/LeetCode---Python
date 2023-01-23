class Dog:
    attr1 = "name"
    attr2 = "dog"

    def fun(self):
        print("1st attribute: ", self.attr1)
        print("2nd attribute: ", self.attr2)


#Object instantiation
Dobarman = Dog()

Dobarman.fun()
print(Dobarman.attr1)
print(Dobarman.attr2)

#With keyword : with keyword is used to wrap the execution of block of code within methods defined by context manager
with open('file path', 'w') as file:
    file.write("hello  !")

