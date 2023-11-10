import random

def generate_random_numbers(start, end, count):
    return [random.randint(start, end) for _ in range(count)]

def shuffle_list(input_list):
    shuffled_list = input_list.copy()
    random.shuffle(shuffled_list)
    return shuffled_list

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))
count = int(input("Enter the number of random numbers: "))

random_numbers = generate_random_numbers(start_range, end_range, count)

shuffled_numbers = shuffle_list(random_numbers)

print("Original List:", random_numbers)
print("Shuffled List:", shuffled_numbers)

'''
Enter the start of the range: 10
Enter the end of the range: 100
Enter the number of random numbers: 8
Original List: [43, 55, 33, 78, 69, 68, 65, 84]
Shuffled List: [84, 69, 33, 43, 55, 65, 78, 68]
'''
