# Resistor Color Expert

## Description

The Resistor Color Expert exercise is a Python programming challenge from Exercism.

The goal is to calculate the resistance value of a resistor based on its color bands and display the result with the correct unit and tolerance.

The program supports resistors with 1, 4, or 5 color bands.

## Color Codes

### Resistor Colors

| Color | Value |
|---|---:|
| Black | 0 |
| Brown | 1 |
| Red | 2 |
| Orange | 3 |
| Yellow | 4 |
| Green | 5 |
| Blue | 6 |
| Violet | 7 |
| Grey | 8 |
| White | 9 |

### Tolerance Colors

| Color | Tolerance |
|---|---:|
| Grey | 0.05% |
| Violet | 0.1% |
| Blue | 0.25% |
| Green | 0.5% |
| Brown | 1% |
| Red | 2% |
| Gold | 5% |
| Silver | 10% |

## How It Works

### 1. One-band resistor
- The single color represents the resistance value.
- Returns the value in ohms.

### 2. Four-band resistor
- First band: First digit.
- Second band: Second digit.
- Third band: Multiplier.
- Fourth band: Tolerance.

### 3. Five-band resistor
- First band: First digit.
- Second band: Second digit.
- Third band: Third digit.
- Fourth band: Multiplier.
- Fifth band: Tolerance.

## Example

**Input:**
```python
resistor_label(["orange", "red", "yellow", "black", "green"])
```

**Calculation:**
- Orange = 3
- Red = 2
- Yellow = 4
- Black = 10⁰ multiplier
- Green = 0.5% tolerance

**Output:**
```text
324 ohms ±0.5%
