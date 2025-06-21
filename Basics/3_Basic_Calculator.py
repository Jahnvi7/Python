n1 = float(input("Enter number : "))
n2 = float(input("Enter another number : "))
o = input("Enter operation (+, -, *, /, %) : ")

# Keep asking for valid operator
vo = ['+', '-', '*', '/', '%']
o = input("Enter operation (+, -, *, /, %) : ")
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
# This code is a basic calculator that performs addition, subtraction, 
# multiplication, division based on user input. It handles division by
# zero and invalid operations gracefully.
