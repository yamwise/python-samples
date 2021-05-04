def findWordFrequencies(sentence):
    words = cleanWords(sentence)
    wordDict = {}

    for word in words:
        word = word.lower()
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1
    return wordDict


def cleanWords(sentence):
    noPunct = ""
    for c in sentence:
        if c.isalpha():
            noPunct = noPunct + c
        elif c == "-" or c == " ":
            noPunct += " "
    return noPunct.split(" ")


sentence = "We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake."


print(findWordFrequencies(sentence))
