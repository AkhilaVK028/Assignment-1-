# defining addition

def addition(operand1, operand2):
    return operand1 + operand2


# defining substraction
def substraction(operand1, operand2):
    return operand1 - operand2


# defining multiply
def multiply(operand1, operand2):
    return operand1 * operand2


# defining division
def divide(operand1, operand2):
    try:
        return operand1 / operand2
    except ZeroDivisionError:
        print("Error: division by zero is undefinable")
        return None


while True:
    try:
        operand1 = float(input("enter the first number"))
        operand2 = float(input("enter the 2nd number"))
    except ValueError:
        print("sorry")
    else:
        break

# mention the variables

operator = input("+ Addition\n - subtraction\n* Multiplication\n/ division\n")
if operator == "+":

    print(operand1, '+', operand2, "=", addition(operand1, operand2))

elif operator == "-":

    print(operand1, "-", operand2, "=", substraction(operand1, operand2))

elif operator == "*":

    print(operand1, "*", operand2, "=", multiply(operand1, operand2))

elif operator == "/":

    print(operand1, "/", operand2, "=", divide(operand1, operand2))

else:

    print("invalid operation")
