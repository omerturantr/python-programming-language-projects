matrix = [
    [2, 5, 8],
    [1, 4, 7],
    [3, 6, 9]
]

total = 0
for i, row in enumerate(matrix):
    for j, value in enumerate(row):
        if i == j:
            total += value * 2
        elif value % 2 == 0:
            total -= value // 2
        else:
            total += value

print(total)
