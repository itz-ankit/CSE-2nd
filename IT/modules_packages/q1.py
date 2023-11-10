def is_palindrome(input1):
    input1= input1.lower()
    return input1 == input1[::-1]

from palindrome import is_palindrome

def main():
    input_string = input("Enter a string: ")
    
    if is_palindrome(input_string):
        print(f'"{input_string}" is a palindrome.')
    else:
        print(f'"{input_string}" is not a palindrome.')

if __name__ == "__main__":
    main()

