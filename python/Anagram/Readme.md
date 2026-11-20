# Anagram – Python

## 1. Problem Description

An anagram is a word created by rearranging the letters of another word.

For example:

- `stone` → `tones`
- `listen` → `silent`
- `earth` → `heart`

The goal of this exercise is to find all anagrams of a given word from a list of candidate words.

### Important Rules

1. Anagrams must contain exactly the same letters.
2. Every letter must appear the same number of times.
3. Uppercase and lowercase letters should be treated equally.
4. The original word itself cannot be considered an anagram.
5. The returned candidates must preserve their original capitalization.

---

## 2. Complete Solution

```python
def find_anagrams(word, candidates):
    target = word.lower()
    sorted_letters = sorted(target)
    result = []

    for candidate in candidates:
        lower_candidate = candidate.lower()

        if lower_candidate != target:
            if sorted(lower_candidate) == sorted_letters:
                result.append(candidate)

    return result
```

---

# 3. Explanation of Every Concept

## A. Function Parameters

```python
def find_anagrams(word, candidates):
```

We define a function called `find_anagrams`.

It receives two parameters:

- `word`: The original word we want to find anagrams for.
- `candidates`: A list of words that we want to check.

Example:

```python
find_anagrams("stone", ["stone", "tones", "banana", "notes"])
```

Here:

- `word = "stone"`
- `candidates = ["stone", "tones", "banana", "notes"]`

**Why don't we define candidates again inside the function?**

Because Python already receives the list through the function parameter.

If we write:

```python
candidates = ["stone", "tones", "banana"]
```

inside the function, we overwrite the original list passed by the caller.

This makes the function less flexible.

---

## B. String Method: `.lower()`

```python
target = word.lower()
```

The `.lower()` method converts all uppercase letters into lowercase letters.

Example:

```python
word = "STONE"

print(word.lower())
