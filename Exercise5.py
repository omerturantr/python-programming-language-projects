data = {
    "a": 3,
    "b": 7,
    "c": 10,
    "d": 5,
    "e": 20
}

total = 0
for key in data:
    value = data[key]
    if value % 2 == 1:
        total += value * 3
    else:
        total += value // 3

print(total)



