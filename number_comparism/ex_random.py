try:   
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter a number: "))
except ValueError:
    print("some of entered values does not seem like integer")
else:
    if number1 > number2:
        print(f"The number {number1} is greater than {number2}")
    elif number1< number2:
        print(f"The number {number2} is greater than {number1}")
    else:
        print("Numbers are equal")
