def compute(values):
    nums = [v * 2 if v % 2 == 0 else v - 1 for v in values]
    return sum(nums)

numbers = [3, 6, 7, 10]
print(compute(numbers))
