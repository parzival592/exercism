def is_isogram(phrase):
    word = phrase.lower()
    letters = set()

    for letter in word:
        if letter in "- ":
            continue
        if letter in letters:
            return False
        letters.add(letter)

    return True
