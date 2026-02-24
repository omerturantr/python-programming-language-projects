def score(values):
    total = 0
    for n in values:
        if n % 4 == 0:
            total += n // 2
        elif n % 2 == 0:
            total += n * 3
        else:
            total -= n
    return total


numbers = [4, 9, 12, 7, 6]
print(score(numbers))
