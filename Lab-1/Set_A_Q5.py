import random

def generate_random_numbers():
    numbers = []
    for i in range(25):
        numbers.append(random.randint(1, 10))
    return numbers

def find_mean(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

def find_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2

def find_mode(numbers):
    frequency = {}
    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
    mode = numbers[0]
    highest_frequency = 0
    for number in frequency:
        if frequency[number] > highest_frequency:
            highest_frequency = frequency[number]
            mode = number
    return mode

random_numbers = generate_random_numbers()
mean = find_mean(random_numbers)
median = find_median(random_numbers)
mode = find_mode(random_numbers)
print("Random Numbers:")
print(random_numbers)
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)