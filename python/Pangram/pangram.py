import string

def is_pangram(sentence):
    alphabet = string.ascii_lowercase
    sentence = sentence.lower()

    for letter in alphabet:
        if letter not in sentence:
            return False

    return True