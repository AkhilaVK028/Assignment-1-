def python_calculator(operand1,operand2,operation):

    if operation == "+":

        return operand1 + operand2

    elif operation == "-":

        return operand1 - operand2

    elif operation == "*":

        return operand1 * operand2

    elif operation == "/":

        return operand1 / operand2

    else :
        return "no operation"

operand1=int(input("enter the 1st number"))

operand2=int(input("enter the 2nd number"))

print("enter '+' to add two number")

print("enter '-' to sub two number")

print("enter '*' to multiply two number")

print("enter '/' to divide two number")

operation=input("choose the operation")

print(python_calculator(operand1,operand2,operation))



