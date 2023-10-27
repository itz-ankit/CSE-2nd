def decimal_to_binary(decimal_num):
    binary_num = ""
    if decimal_num == 0:
        return "0"
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_num = str(remainder) + binary_num
        decimal_num = decimal_num // 2
    return binary_num


def binary_to_decimal(binary_num):
    decimal_num = 0
    binary_num = binary_num[::-1]  # Reverse the binary string
    for i in range(len(binary_num)):
        if binary_num[i] == '1':
            decimal_num += 2**i
    return decimal_num


def decimal_to_octal(decimal_num):
    octal_num = ""
    if decimal_num == 0:
        return "0"
    while decimal_num > 0:
        remainder = decimal_num % 8
        octal_num = str(remainder) + octal_num
        decimal_num = decimal_num // 8
    return octal_num


def octal_to_decimal(octal_num):
    decimal_num = 0
    octal_num = octal_num[::-1]  # Reverse the octal string
    for i in range(len(octal_num)):
        digit = int(octal_num[i])
        decimal_num += digit * (8**i)
    return decimal_num


def decimal_to_hexadecimal(decimal_num):
    hexadecimal_num = ""
    if decimal_num == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"
    while decimal_num > 0:
        remainder = decimal_num % 16
        hexadecimal_num = hex_chars[remainder] + hexadecimal_num
        decimal_num = decimal_num // 16
    return hexadecimal_num


def hexadecimal_to_decimal(hexadecimal_num):
    decimal_num = 0
    hex_chars = "0123456789ABCDEF"
    hexadecimal_num = hexadecimal_num.upper()
    hexadecimal_num = hexadecimal_num[::-1]  # Reverse the hexadecimal string
    for i in range(len(hexadecimal_num)):
        digit = hex_chars.index(hexadecimal_num[i])
        decimal_num += digit * (16**i)
    return decimal_num


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
