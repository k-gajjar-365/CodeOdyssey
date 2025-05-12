# from art_calculator import logo
import art_calculator
print(art_calculator.logo)
# ASCII art for calculator 
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# print(operations["*"](4, 8))


def calculator():
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()

#**********************************************************
#******************* Method - 2 ***************************
#**********************************************************
# from art import logo
# print(logo)
#
# def add(a,b):
#     """return sum of 2 numbers"""
#     return a+b
#
# def sub(a,b):
#     """return subtraction of two numbers"""
#     return a-b
#
# def div(a,b):
#     """returns division of 2 numbers"""
#     if b==0:
#         return "Zero cannot divide by any number"
#     else:
#         if (a/b)%1==0:
#             return a//b
#         else:
#             return round((a/b),2)
#
# def mul(a,b):
#     """Return Multiplication of 2 numbers"""
#     return a*b
#
# operations = {
#     "+":add,
#     "-":sub,
#     "*":mul,
#     "/":div,
# }
#
# result = 0
# a_include=True
# while True:
#     if a_include:
#         a = int(input("Enter first number : "))
#     print("+\n-\n*\n/")
#     op = input("Enter operator : \n")
#     b = int(input("Enter second number : "))
#     if op=="+":
#         result=add(a,b)
#     elif op=="-":
#         result=sub(a,b)
#     elif op=="*":
#         result=mul(a,b)
#     elif op=="/":
#         result=div(a,b)
#     else:
#         print("Please enter valid Operator!")
#
#     print(f"Result : {result}")
#
#     should_continue=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
#     if should_continue=="n":
#         print("\n"*20)
#         a_include=True
#     elif should_continue=="y":
#         a_include=False
#         a=result
#