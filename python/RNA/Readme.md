# DNA to RNA Transcription 🧬

## 📌 About the Project

This project implements a simple DNA-to-RNA transcription function using Python.

The goal is to convert a given DNA sequence into its complementary RNA sequence by replacing each DNA nucleotide with its corresponding RNA nucleotide.

This exercise is part of learning Python through biological and computational problems.

## 🧬 Biological Background

DNA and RNA consist of four types of nucleotides.

The transcription rules are:

| DNA | RNA |
|:---:|:---:|
| G | C |
| C | G |
| T | A |
| A | U |

## ⚙️ How It Works

The `to_rna()` function:

1. Accepts a DNA sequence as a string.
2. Iterates through each nucleotide.
3. Validates whether each character is a valid DNA nucleotide.
4. Converts each nucleotide into its RNA complement.
5. Builds and returns the resulting RNA sequence.
6. Raises a `ValueError` if an invalid nucleotide is provided.

## 💻 Example

**Input:**
```python
to_rna("ACGT")
```

**Output:**
```python
"UGCA"
```

Another example:

**Input:**
```python
to_rna("GGGCCC")
```

**Output:**
```python
"CCCGGG"
```

## 🚨 Error Handling

If the input contains an invalid nucleotide, the function raises a `ValueError`.

Example:

```python
to_rna("AGXT")
```

Output:
```python
ValueError: It is not a valid nucleotide.
```

## 🛠️ Technologies Used

- Python 3
- String manipulation
- For loops
- Conditional statements (`if/elif`)
- Exception handling (`ValueError`)

## 📚 What I Learned

Through this exercise, I practiced:

- Iterating over strings using `for` loops.
- Checking characters using the `in` operator.
- Using conditional statements to map values.
- Building strings using the `+=` operator.
- Handling invalid input with exceptions.
- Understanding DNA-to-RNA complementary nucleotide mapping.

## 🎯 Purpose

The purpose of this exercise is to strengthen Python fundamentals and develop problem-solving skills through practical programming challenges.

---

**Author:** [Your GitHub Username]

**Language:** Python 3
