def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return "Factorial is not defined for negative numbers"
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

from fact import factorial

def main():
    try:
        num = int(input("Enter a non-negative integer: "))
        result = factorial(num)
        if type(result) == str:
            print(result)
        else:
            print(f"The factorial of {num} is {result}")
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")

if __name__ == "__main__":
    main()
