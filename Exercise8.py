records = {
    "x": [4, 7, 2],
    "y": [5, 10, 3],
    "z": [6, 1, 9]
}

total = 0
for key in records:
    nums = records[key]
    for n in nums:
        if n % 3 == 0:
            total += n * 2
        elif n % 2 == 0:
            total -= n // 2
        else:
            total += n

print(total)



