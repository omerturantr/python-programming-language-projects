def transform(nums):
    result = 0
    for i, n in enumerate(nums):
        if i % 2 == 0:
            result += n * 2
        else:
            result -= n // 2
    return result

values = [5, 8, 3, 10, 6]
print(transform(values))


