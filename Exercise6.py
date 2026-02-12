def analyze(nums):
    even_sum = 0
    odd_sum = 0
    for n in nums:
        if n % 2 == 0:
            for i in range(1, 4):
                even_sum += n // i
        else:
            for i in range(2):
                odd_sum += n * (i + 1)
    return even_sum - odd_sum

numbers = [4, 7, 10, 3]
print(analyze(numbers))

