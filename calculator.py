# ============================================
#         PYTHON BASICS CALCULATOR
# ============================================

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a % b

def power(a, b):
    return a ** b


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  Invalid input. Please enter a valid number.")


def show_menu():
    print("\n" + "=" * 40)
    print("         PYTHON BASICS CALCULATOR")
    print("=" * 40)
    print("  1.  Addition       (+)")
    print("  2.  Subtraction    (-)")
    print("  3.  Multiplication (*)")
    print("  4.  Division       (/)")
    print("  5.  Modulus        (%)")
    print("  6.  Power          (**)")
    print("  0.  Exit")
    print("=" * 40)


def main():
    print("\nWelcome to the Python Basics Calculator!")

    while True:
        show_menu()
        choice = input("\n  Enter your choice (0–6): ").strip()

        if choice == "0":
            print("\n  Goodbye! Thanks for using the calculator.\n")
            break

        if choice not in ("1", "2", "3", "4", "5", "6"):
            print("  Invalid choice. Please select a number from 0 to 6.")
            continue

        a = get_number("  Enter first number:  ")
        b = get_number("  Enter second number: ")

        operations = {
            "1": (add,      "+",  "Addition"),
            "2": (subtract, "-",  "Subtraction"),
            "3": (multiply, "*",  "Multiplication"),
            "4": (divide,   "/",  "Division"),
            "5": (modulus,  "%",  "Modulus"),
            "6": (power,    "**", "Power"),
        }

        func, symbol, name = operations[choice]
        result = func(a, b)

        # Format nicely: show int if result is a whole number
        if isinstance(result, float) and result == int(result):
            result_display = int(result)
        else:
            result_display = result

        print(f"\n  {name}: {a} {symbol} {b} = {result_display}")


if __name__ == "__main__":
    main()
