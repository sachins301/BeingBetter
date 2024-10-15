"""
Rolling Average Calculation: 
Implement a function that takes a stream of numbers or user activities and returns a rolling average over a specified window size.
"""

def rolling_average(numbers, window_size):
    res = []
    for i in range(len(numbers) - window_size + 1):
        window_sum = sum(numbers[i : i+window_size])
        res.append(window_sum / window_size)
    return res




numbers = [10, 20, 30, 40, 50]
print(rolling_average(numbers, 3))