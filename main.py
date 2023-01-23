

#UnboundLocalError: local variable 'input' referenced before assignment

def main():
    print("Started")
    output = getInteger()
    print(output)

def getInteger():
    inp = int(input("Enter a number : "))
    return inp

if __name__ == "__main__":
    main()