import numpy as np

def calculate_sum(numbers):
    total = 0
    for num in numbers:  # Loop-based sum (inefficient)
        total += num
    return total
