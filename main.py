from calculator import Calculator


def main():
    calc = Calculator()
    print("Simple Calculator")
    print("Operations: + (addition), - (subtraction), * (multiplication), q (quit)")

    while True:
        user_input = input("\nEnter expression (e.g. 3 + 5): ").strip()
        if user_input.lower() == "q":
            break

        parts = user_input.split()
        if len(parts) != 3:
            print("Invalid input. Use format: <number> <+|-> <number>")
            continue

        try:
            a = float(parts[0])
            op = parts[1]
            b = float(parts[2])
        except ValueError:
            print("Invalid numbers.")
            continue

        if op == "+":
            print(f"Result: {calc.add(a, b)}")
        elif op == "-":
            print(f"Result: {calc.subtract(a, b)}")
        elif op == "*":
            print(f"Result: {calc.multiply(a, b)}")
        else:
            print(f"Unknown operator '{op}'. Use +, - or *.")


if __name__ == "__main__":
    main()
