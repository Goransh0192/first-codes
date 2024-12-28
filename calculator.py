'''                                       Calculator
This program is a simple calculator that takes two numbers and an operation as input and returns the 
result of the operation.'''

while True:
    input_a = float(input("Enter the first number: "))
    input_b = float(input("Enter the second number: "))

    operation = input("Please enter the operation (+, -, *, /): ")

    if operation == '+':
        print(f"The result is: {input_a + input_b}")
    elif operation == '-':
        print(f"The result is: {input_a - input_b}")
    elif operation == '*':
        print(f"The result is: {input_a * input_b}")
    elif operation == '/':
        if input_b != 0:
            print(f"The result is: {input_a / input_b}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation")
    again = input("Do you want to perform another calculation? (yes/no): ")
    if again.lower() != "yes":
        break