def multiplication(first_number, second_number):
    return first_number * second_number
def division(first_number, second_number):
    # Handle division by zero
    if second_number == 0:
        return "Error: Division by zero!"
    return first_number / second_number
def addition(first_number, second_number):
    return first_number + second_number
def subtraction(first_number, second_number):
    return first_number - second_number
def calculator():
    result = 0
    continue_calculating = True
    while continue_calculating:
        # If result is 0, start fresh; otherwise, continue with the result
        if result == 0:
            first_number = int(input("What's the first number?: "))
        else:
            first_number = result
        # Get user input
        operation = input("Pick an operation (+, -, *, /): ")
        second_number = int(input("What's the next number?: "))
        # Perform the selected operation
        if operation == "+":
            result = addition(first_number, second_number)
        elif operation == "-":
            result = subtraction(first_number, second_number)
        elif operation == "*":
            result = multiplication(first_number, second_number)
        elif operation == "/":
            result = division(first_number, second_number)
        else:
            print("Invalid operation. Please try again.")
            continue
        # Show the result
        print(f"The result is: {result}")
        # Ask user whether to continue
        user_choice = input(f"Type 'y' to continue calculating with {result}, or 'n' to start a new calculation: ").lower()
        if user_choice == "n":
            result = 0
            print("Starting a new calculation.")
        elif user_choice != "y":
            continue_calculating = False
            print("Goodbye!")
# Start the calculator
calculator()