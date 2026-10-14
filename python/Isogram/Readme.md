# Isogram — Python

## 📌 About the Exercise

An **isogram** is a word or phrase in which no letter appears more than once.

Spaces and hyphens are allowed and should be ignored when checking for repeated letters. Uppercase and lowercase letters are treated as the same letter.

The goal of this exercise is to implement a Python function that determines whether a given word or phrase is an isogram.

## 🎯 Examples

| Input            | Output  | Explanation                                                     |
| ---------------- | ------- | --------------------------------------------------------------- |
| `"lumberjacks"`  | `True`  | Every letter appears once.                                      |
| `"background"`   | `True`  | No letters repeat.                                              |
| `"downstream"`   | `True`  | All letters are unique.                                         |
| `"six-year-old"` | `True`  | Hyphens are ignored, and no letter repeats.                     |
| `"isograms"`     | `False` | The letter `s` appears twice.                                   |
| `"hello"`        | `False` | The letter `l` appears twice.                                   |
| `"Alphabet"`     | `False` | Uppercase `A` and lowercase `a` are treated as the same letter. |
| `"up-to-date"`   | `False` | The letter `t` repeats.                                         |

## 🛠️ Technologies and Concepts

* **Language:** Python 3
* **Topics:** Functions, strings, loops, conditional statements, sets, membership operators, and Boolean values.

## 💻 Solution

```python
def is_isogram(phrase):
    word = phrase.lower()
    letters = set()

    for letter in word:
        if letter in " -":
            continue

        if letter in letters:
            return False

        letters.add(letter)

    return True
```

## 🧠 How the Solution Works

### 1. Convert the phrase to lowercase

```python
word = phrase.lower()
```

The `.lower()` method converts uppercase letters to lowercase.

For example:

```python
phrase = "Alphabet"
word = phrase.lower()

print(word)
```

Output:

```text
alphabet
```

