# Calculator

#Add
def add (n1,n2):
    "Adds both variable up together"
    return  n1 + n2

#Subtract
def subtract (n1,n2):
    "Subtract the right variable from the left variable"
    return n1 - n2

#Multiply 
def multiply (n1,n2):
    "Return the product of both variables"
    return n1 * n2

#divide
def division (n1,n2):
    "return the division of the left variable divided by the right variable"
    return n1 / n2

operations =  {
    "+":add,
    '-':subtract,
    '*':multiply,
    '/':division
}

num1 = int(input ("What's the first number?: "))

num2 = int(input("Whats the second number?: "))

for key in operations:
    print(key)

operation_key = input("Pick an operation from the line above: ")

output = operations[operation_key](num1,num2)

print(f"{num1} {operation_key} {num2} = {output}")