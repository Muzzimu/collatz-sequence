# Collatz Sequence Project

This project contains a Python program that demonstrates the Collatz sequence, a mathematical sequence that eventually reaches 1 for any positive integer input.

## Overview

The Collatz sequence is defined as follows:

- Start with any positive integer `n`.
- If `n` is even, the next number in the sequence is `n / 2`.
- If `n` is odd, the next number in the sequence is `3n + 1`.
- Repeat the process until `n` becomes 1.

This project includes a Python script that:
1. Prompts the user to enter an integer.
2. Applies the Collatz sequence to the integer.
3. Prints each step of the sequence until it reaches 1.

## Requirements

- Python 3.x

## How to Run

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Muzzimu/collatz-sequence.git
    cd collatz-sequence
    ```

2. **Run the script:**
    ```bash
    python collatz.py
    ```

3. **Enter an integer:**
    - When prompted, input a positive integer to see the Collatz sequence in action.

## Example

```plaintext
$ python collatz.py
Enter an integer: 6
3
10
5
16
8
4
2
1
