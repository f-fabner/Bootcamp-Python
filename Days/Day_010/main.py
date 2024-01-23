def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

num1 = int(input(f"what's the first number?\n"))
num2 = int(input(f"what's the second number?\n"))
for symbol in operations:
    print(symbol)
operation_symbol = input(f"Pick an operation from the line above:\n")
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")