word = "Navigating"

word_letters = []

for letters in word:
    word_letters.append(letters)

print(*word_letters)
word_letters.pop(3)
print(*word_letters)