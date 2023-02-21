germanDictionary = {"hello": "hallo", "how": "wie", "are": "gehts", "you": "dir"}
englishPhrase = input("enter an eng word or phrase to translate")
englishWords = englishPhrase.lower().split()
germanWords = []
for word in englishWords:
    if word in germanDictionary:
        germanWords.append(germanDictionary[word])
else:
    germanWords.append(word)
print("in german, say:", " ".join(germanWords))

