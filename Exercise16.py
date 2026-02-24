values = [11, 14, 3, 18, 5, 20]

index = 0
result = 0
while index < len(values):
    n = values[index]
    if index % 2 == 0:
        if n % 2 == 0:
            result += n // 2
        else:
            result += n * 2
    else:
        result -= n - 1
    index += 1

print(result)
