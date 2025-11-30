running = True

while running:

    try:
        first = int(input('Give me the first number for the addition '))
        second = int(input('Give me the second number for the addition '))
        result = first / second
        print(f"The result is: {result}")
        running = False
    except ValueError:
        print("Your input should be a number")
        running = False

