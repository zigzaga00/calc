def result(x, op, y):
    # get and return the result
    return ops[op](x, y)

def calculator():
    # get the user supplied input
    a = int(input("\nFirst number: "))
    print("\nChoose one of the following operations: ")
    # use a for loop to iterate through possible operation inputs
    for k in ops:
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
# using expression based functions (lambdas)
ops = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y
}

calculator()
