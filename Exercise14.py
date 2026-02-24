text = "Python Practice Session"

counts = {
    "vowels": 0,
    "consonants": 0
}

for ch in text.lower():
    if ch.isalpha():
        if ch in "aeiou":
            counts["vowels"] += 1
        else:
            counts["consonants"] += 1

result = counts["consonants"] - counts["vowels"]
print(result)
