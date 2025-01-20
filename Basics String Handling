# Request a phrase from the user
phrase = input("Enter a phrase: ")

character_phrase = []
split_phrase = phrase.split()
word_phrase = []


# Make alternate characters upper and lower case
for i in range(len(phrase)):

    if i % 2 == 0:
        character_phrase.append(phrase[i].upper())

    else:
        character_phrase.append(phrase[i].lower())

character_phrase = "".join(character_phrase)
print(character_phrase)

# Make alternate words upper and lower case
for index, word in enumerate(split_phrase):
    if index % 2 == 0:
        word_phrase.append(word.upper())
    else:
        word_phrase.append(word.lower())

word_phrase = " ".join(word_phrase)
print(word_phrase)
