"Calculator but more advanced than the basic calculator."
import math

def calculate(operation, a, b=None):
    if operation == 1:
        return a + b
    elif operation == 2:
        return a - b
    elif operation == 3:
        return a * b
    elif operation == 4:
        if b != 0:
            return a / b
        else:
            return "fah"
    elif operation == 5:
        return math.pow(a, b)
    elif operation == 6:
        if a < 0:
            return "faaah"
        else:
            return math.sqrt(a)
    else:
        if a < 0:
            return "faah"
        elif a % 1 != 0:
            return "faaaah"
        else:
            return math.factorial(int(a))
        

print("Welcome to the advanced calculator!!!")

previous_result = None
while True:
    operation = int(input("Choose operation\n1. add\t\t2. subtract\t\t3. multiply\t\t4. divide\n5. power\t6. square root\t\t7. factorial\n(Choose from 1,2,3,4,5,6,7)\n"))
    if previous_result is not None:
        a = previous_result
        if operation in range(1,6):
            b = float(input("Enter the number: "))
    else:
        if operation in range(1,6):
            a = float(input("Enter the number: "))
            b = float(input("Enter the number: "))
        elif operation in range(6,8):
            a = float(input("Enter the number: "))
            b = None
        else:
            print("Invalid operation!!!\nRestarting calculator...")
            continue
    res = calculate(operation,a,b)
    if res == "fah":
        print("Division by 0 is not possible!!!\nRestarting calculator...")
        continue
    elif res == "faah":
        print("Factorial of a negative number is not defined!!!\nRestarting calculator...")
        continue
    elif res == "faaah":
        print("Square root of a negative number is not defined!!!\nRestarting calculator...")
        continue
    elif res == "faaaah":
        print("Factorial of a non-integer number is not defined!!!\nRestarting calculator...")
        continue
    else:
        print(f"The result is: {res}")

    ask = input("Use this result for another calculation? (yes/no): ")
    if ask.lower() == "yes":
        previous_result = res
    else:
        previous_result = None
    ask2 = input("Do you want to use the calculator again? (yes/no): ")
    if ask2.lower() != "yes":
        break
 