# Pangram — Python Exercise

## 📌 Overview

A **pangram** is a sentence that contains every letter of the English alphabet at least once.

In this exercise, I created a Python function that checks whether a sentence is a pangram. The function is case-insensitive, meaning uppercase and lowercase letters are treated equally.

### Examples

```python
is_pangram("The quick brown fox jumps over the lazy dog")
# True

is_pangram("Hello world")
# False

is_pangram("abcdefghijklmnopqrstuvwxyz")
# True
```

## 🛠️ Solution

```python
import string

def is_pangram(sentence):
    alphabet = string.ascii_lowercase
    sentence = sentence.lower()

    for letter in alphabet:
        if letter not in sentence:
            return False

    return True
```

## 🧠 How It Works

### 1. Import the `string` module

```python
import string
```

The `string` module provides useful string constants and operations.

### 2. Get the English alphabet

```python
alphabet = string.ascii_lowercase
```

`string.ascii_lowercase` contains all 26 lowercase English letters:

`abcdefghijklmnopqrstuvwxyz`

It is an attribute, not a function, so parentheses are not required.

