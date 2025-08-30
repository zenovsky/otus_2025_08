import numbers


def calculate_average(nums):
    total = sum(nums)
    count = len(numbers)
    average = total / count


nums = [10, 15, 20]
result = calculate_average(nums)
print("The average is:", result)
