# calculator
# version 1.2
# created by zvfaatl
 
while True:  # infinite cycle input for data
 
    i = input("Select action (+,-,*,/,**,//,pcircle,pquadrate,exit,vat): ")  # check selected action
    if i == "exit":  # condition check for exit
        print("Goodbye!")  # output result
        result = exit()  # exit operation
    if i == "vat":  # condition check for vat
        a = float(input("Enter first number: "))  # enter first number
        vat = 20  # % vat
        result = a + (a * vat / 100)  # vat operation
        print("Result: " + str(result))  # output result
        print()  # empty line
    elif i == "pcircle":
        a = float(input("Enter first number: "))  # enter first number
        pi = 3.14  # number pi
        result = a * pi  # output result
        print("Result: " + str(result))  # output result
        print()  # empty line
        continue
    elif i == "pquadrate":
        a = float(input("Enter first number: "))  # enter first number
        result = 4 * a  # output result
        print("Result: " + str(result))  # output result
        print()  # empty line
    elif i < "vat":
        a = float(input("Enter first number: "))  # enter first number
        b = float(input("Enter second number: "))  # enter second number
 
        if i == "+":  # condition check for addition
            result = a + b  # addition operation
            print("Result: " + str(result))  # output result
            print()  # empty line
        elif i == "-":  # condition check for subtraction
            result = a - b  # subtraction operation
            print("Result: " + str(result))  # output result
            print()  # empty line
        elif i == "*":  # condition check for multiplication
            result = a * b  # multiplication operation
            print("Result: " + str(result))  # output result
            print()  # empty line
        elif i == "/":  # condition check for division
            if not b == float(0):  # check b > 0
                result = a / b  # division operation
                print("Result: " + str(result))  # output result
                print()  # empty line
            else:  # differently if b < 0
                print("Wrong action")  # output comment about error
                print()  # empty line
        elif i == "**":  # condition check for exponentiation
            result = a ** b  # exponentiation operation
            print("Result: " + str(result))  # output result
            print()  # empty line
        elif i == "//":  # condition check for division without remainder
            result = a // b  # division without remainder operation
            print("Result: " + str(result))  # output result
            print()  # empty line
        else:  # select wrong action
            print("Wrong action!")  # output comment about error wrong action
            print()  # empty line
 
