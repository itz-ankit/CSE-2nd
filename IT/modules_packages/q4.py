import random
import statistics

numbers = [random.randint(1, 10) for _ in range(10)]

mean = statistics.mean(numbers)

median = statistics.median(numbers)

std_dev = statistics.stdev(numbers)

# Print the results
print("Random numbers:", numbers)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)

'''
Random numbers: [8, 3, 10, 9, 6, 10, 8, 2, 2, 5]
Mean: 6.3
Median: 7.0
Standard Deviation: 3.1640339933558095
'''