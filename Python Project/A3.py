def decimal_to_binary(decimal_num):
    return bin(decimal_num)[2:]


def binary_to_decimal(binary_num):
    return int(binary_num, 2)


def decimal_to_octal(decimal_num):
    return oct(decimal_num)[2:]


def octal_to_decimal(octal_num):
    return int(octal_num, 8)


def decimal_to_hexadecimal(decimal_num):
    return hex(decimal_num)[2:]


def hexadecimal_to_decimal(hexadecimal_num):
    return int(hexadecimal_num, 16)


while True:
    print("\nNumber Converter Menu:")
    print("1. Decimal to Binary")
    print("2. Binary to Decimal")
    print("3. Decimal to Octal")
    print("4. Octal to Decimal")
    print("5. Decimal to Hexadecimal")
    print("6. Hexadecimal to Decimal")
    print("7. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6/7): ")

    if choice == '1':
        decimal_num = int(input("Enter a decimal number: "))
        binary_num = decimal_to_binary(decimal_num)
        print(f"Binary: {binary_num}")

    elif choice == '2':
        binary_num = input("Enter a binary number: ")
        decimal_num = binary_to_decimal(binary_num)
        print(f"Decimal: {decimal_num}")

    elif choice == '3':
        decimal_num = int(input("Enter a decimal number: "))
        octal_num = decimal_to_octal(decimal_num)
        print(f"Octal: {octal_num}")

    elif choice == '4':
        octal_num = input("Enter an octal number: ")
        decimal_num = octal_to_decimal(octal_num)
        print(f"Decimal: {decimal_num}")

    elif choice == '5':
        decimal_num = int(input("Enter a decimal number: "))
        hexadecimal_num = decimal_to_hexadecimal(decimal_num)
        print(f"Hexadecimal: {hexadecimal_num}")

    elif choice == '6':
        hexadecimal_num = input("Enter a hexadecimal number: ")
        decimal_num = hexadecimal_to_decimal(hexadecimal_num)
        print(f"Decimal: {decimal_num}")

    elif choice == '7':
        print("Exiting the Number Converter. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")
