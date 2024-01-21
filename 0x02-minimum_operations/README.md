# 0-minoperations.py

This Python script contains a function `find(number)`. The function takes an integer as an argument and performs certain operations on it.

## Function Details

- `find(number)`: This function takes an integer `number` as input. It initializes two variables `res` and `i` to 0 and 2 respectively, and `pri` to 1. It then enters a while loop which continues until `i` is less than or equal to `number`. Inside the loop, it checks if `number` is divisible by `i`. If it is, it updates `pri` to `i`, increments `i` by `pri` and `res` by 2. If `number` is not divisible by `i`, it increments `i` by `pri` and `res` by 1. The function finally returns `res`.

## Usage

To use this script, import it in your Python program and call the `find` function with an integer argument.

```python
import minoperations

result = minoperations.find(10)
print(result)