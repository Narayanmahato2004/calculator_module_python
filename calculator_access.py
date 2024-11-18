# main.py

# Importing the calculator module
import calculator

def main():
    print("Welcome to the Python Calculator!")

    # Using the calculator functions
    a = 10
    b = 5

    print(f"{a} + {b} = {calculator.add(a, b)}")
    print(f"{a} - {b} = {calculator.subtract(a, b)}")
    print(f"{a} * {b} = {calculator.multiply(a, b)}")
    print(f"{a} / {b} = {calculator.divide(a, b)}")
    print(f"{a} ^ {b} = {calculator.power(a, b)}")
    print(f"Square root of {a} = {calculator.sqrt(a)}")
    print(f"Square root of -9 = {calculator.sqrt(-9)}")  # Testing with a negative value

if __name__ == "__main__":
    main()
