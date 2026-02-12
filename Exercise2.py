def check(nums):
    count = 0
    for n in nums:
        if n % 3 == 0 and n % 2 != 0:
            count += n
    return count

values = [3, 4, 6, 9, 10, 15]
print(check(values))