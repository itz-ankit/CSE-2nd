import random

count = int(input("Enter the number of random numbers: "))

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

random_numbers = [random.randint(start_range, end_range) for i in range(count)]

print("Random Numbers:", random_numbers)

'''
Enter the number of random numbers: 5
Enter the start of the range: 10
Enter the end of the range: 100
Random Numbers: [66, 13, 98, 63, 22]
'''
