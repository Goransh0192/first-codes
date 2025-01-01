#project 3
#temperature convertor

def temp_conv_celsius_to_fahrenheit():
    celsius = float(input("Please enter the temperature in celsius: "))
    fahrenheit = ((celsius*(9/5)) + 32)
    return fahrenheit

def temp_conv_celsius_to_kelvin():
    celsius = float(input("Please enter the temperature in celsius: "))
    kelvin = celsius + 273.15
    return kelvin

def temp_conv_fahrenheit_to_celsius():
    fahrenheit = float(input("Please enter the temperature in fahrenheit: "))
    celsius = ((fahrenheit - 32)*(5/9))
    return celsius

def temp_conv_fahrenheit_to_kelvin():
    fahrenheit = float(input("Please enter the temperature in fahrenheit: "))
    kelvin = ((fahrenheit + 459.67)*(5/9))
    return kelvin

def temp_conv_kelvin_to_celsius():
    kelvin = float(input("Please enter the temperature in kelvin: "))
    celsius = kelvin - 273.15
    return celsius

def temp_conv_kelvin_to_fahrenheit():
    kelvin = float(input("Please enter the temperature in kelvin: "))
    fahrenheit = ((kelvin - 273.15)*(9/5)) + 32
    return fahrenheit

running = True
while running:
    print("temperature convertor".title())
    print("1.celsius to fahrenheit\n2.celsius to kelvin\n3.fahrenheit to celsius\n4.fahrenheit to kelvin\n5.kelvin to celsius\n6.kelvin to fahrenheit\n7.exit the program".title())

    user_input = int(input("please choose the option: ".title()))

    if user_input == 1:
        result = temp_conv_celsius_to_fahrenheit()
        print(f"{result} degree fahrenheit")
    elif user_input == 2:
        result = temp_conv_celsius_to_kelvin()
        print(f"{result} degree kelvin")
    elif user_input == 3:
        result = temp_conv_fahrenheit_to_celsius()
        print(f"{result} degree celsius")
    elif user_input == 4:
        result = temp_conv_fahrenheit_to_kelvin()
        print(f"{result} degree kelvin")
    elif user_input == 5:
        result = temp_conv_kelvin_to_celsius()
        print(f"{result} degree celsius")
    elif user_input == 6:
        result = temp_conv_kelvin_to_fahrenheit()
        print(f"{result} degree fahrenheit")
    elif user_input == 7:
        running = False
        print("Thank you for using the Temperature Convertor.")
        break
    else:
        print("Invalid input")
    again = input("Do you want to use the program again: (yes/no)").strip().lower()
    if again != "yes":
        print("Thank you for using the Temperature Convertor.")
        break

