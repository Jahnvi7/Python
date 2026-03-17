def Validity():
    while True:
        try:
            n1 = float(input("Enter number : "))
            n2 = float(input("Enter another number : "))
        except ValueError:
            print("Invalid input. Please enter number(s)")
        else:
            break
    return n1, n2

while True:
    n1, n2 = Validity()
    o = input("Enter operation (+, -, *, /, %) : ")

    # Keep asking for valid operator
    vo = ['+', '-', '*', '/', '%']
    while o not in vo:
        print("Invalid operation. Please enter one of +, -, *, /, %.")
        o = input("Enter operation again: ")

    # Perform the operation
    if o == '+':
        r = n1 + n2
    elif o == '-':
        r = n1 - n2
    elif o == '*':
        r = n1 * n2
    elif o == '/':
        if n2 != 0:
            r = n1 / n2
        else:
            r = "INFINITY!"
    elif o == '%':
        if n2 != 0:
            r = n1 % n2
        else:
            r = "Cannot perform modulo by zero!"
    else:
        r = "Invalid operation. Please enter one of +, -, *, /, or %."
    print("Your result is :", r)

    # Ask if the user wants to calculate again
    while True:
        duw = input("Do you want to calculate? (yes/no) : ").strip().lower()
        if duw == 'yes':
            break
        elif duw not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
        elif duw == 'no':
            print("Thanks for calculating :)")
            exit()

'''
This code is a basic calculator that performs addition, subtraction, multiplication, division based on user input.
It handles division by zero and invalid operations gracefully.
'''