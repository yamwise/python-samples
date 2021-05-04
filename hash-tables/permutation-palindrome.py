def checkWord(word):
    letters = set()

    for c in word:
        if c not in letters:
            letters.add(c)
        else:
            letters.remove(c)

    if len(letters) % 2 == 0:
        return len(letters) == 0
    else:
        return len(letters) == 1


inputs = ["civic", "ivicc", "civil", "livci"]

for word in inputs:
    print(checkWord(word))
