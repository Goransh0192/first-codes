#copilot made this

input_a = float(input("Enter the first no."))
input_b = float(input("Enter the second number: "))

userinput=input("pls enter the operation from +,-,*,/  ")

if userinput == '+':
    print(input_a + input_b)
elif userinput == '-':    
    print(input_a - input_b)
elif userinput == '*':
    print(input_a * input_b)
elif userinput == '/':
    print(input_a / input_b)
else:
    print("Invalid input")
