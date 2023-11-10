def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True

def prime_range(start, end):
    primes = []
    for num in range(max(2, start), end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

from prime_checker import prime_range

def main():
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))

    prime_numbers = prime_range(start, end)
    if prime_numbers:
        print(f"Prime numbers between {start} and {end}:")
        print(prime_numbers)
    else:
        print(f"No prime numbers found between {start} and {end}.")

if __name__ == "__main__":
    main()

