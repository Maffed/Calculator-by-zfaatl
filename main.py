# calculator
# version 1.3
# created by zvfaatl
 
while True:  # infinite cycle input for data
 
    i = input("Select action (+,-,*,/): ")  # check selected action (+,-,*,/)
    a = float(input("Enter first number: "))  # enter first number
    b = float(input("Enter second number: "))  # enter second number
 
    if i == "+":  # condition check for addition
        result = a + b  # addition operation
        print("Result: " + str(result))  # output result|
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
 
    else:  # select wrong action
        print("Wrong action!")  # output comment about error wrong action
        print()  # empty line
