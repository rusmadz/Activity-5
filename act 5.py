def divide(num1, num2):
    """
    Performs division with validation for zero denominator
    Returns None if denominator is zero
    """
    if num2 == 0:
        print("Error: Denominator cannot be zero")
        return None
    return num1 / num2

def exponentiation(base, exponent):
    """
    Performs exponentiation (base raised to the power of exponent)
    """
    return base ** exponent

def remainder(num1, num2):
    """
    Calculates remainder with validation for zero denominator
    Returns None if denominator is zero
    """
    if num2 == 0:
        print("Error: Denominator cannot be zero")
        return None
    return num1 % num2

def summation(start, end):
    """
    Calculates sum of numbers from start to end (inclusive)
    Returns None if end is less than or equal to start
    """
    if end <= start:
        print("Error: Second number must be greater than first number")
        return None
    return sum(range(start, end + 1))

def display_menu():
    """Displays the operation menu"""
    print("\nMathematical Operations Menu:")
    print("[D] - Divide")
    print("[E] - Exponentiation")
    print("[R] - Remainder")
    print("[F] - Summation")
    print("[Q] - Quit")

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice: ").upper()

        if choice == 'Q':
            print("Thank you for using the calculator!")
            break

        if choice not in ['D', 'E', 'R', 'F']:
            print("Invalid choice! Please select a valid operation.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            result = None
            if choice == 'D':
                result = divide(num1, num2)
            elif choice == 'E':
                result = exponentiation(num1, num2)
            elif choice == 'R':
                result = remainder(num1, num2)
            elif choice == 'F':
                # Convert to integers for summation
                result = summation(int(num1), int(num2))

            if result is not None:
                print(f"\nResult: {result}")

        except ValueError:
            print("Error: Please enter valid numbers")

if __name__ == "__main__":
    main()
