

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def result(x, op, y):
    # get and return the result
    return operations[op](x, y)

def calculator():
    # get the user supplied input
    a = int(input("\nFirst number: "))
    print("\nChoose one of the following operations: ")
    # use a for loop to iterate through possible operation inputs
    for k in operations:
        print(k)
    again = True
    while again:
        choice = input("\nEnter your choice of operation: ")
        b = int(input("\nEnter the next number: "))
        answer = result(a, choice, b)
        print(answer)
        cont = int(input("\nDo you want to (1) continue this calculation or (2) start a new calculation? "))
        if cont == 1:
            a = answer
        elif cont == 2:
            calculator()
# main
# put the four operations into a dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

calculator()
