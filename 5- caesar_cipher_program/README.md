# Caesar Cipher Program v2

> Updated version of the Caesar Cipher from the Python course ([https://www.udemy.com/course/100-days-of-code/](https://www.udemy.com/course/100-days-of-code/))

Python exercise focused on learning:

* `input()` and user interaction
* `for` loops and iteration
* Conditional statements (`if`, `elif`, `else`)
* Working with lists and `append()`
* String manipulation using `"".join()`
* Functions and modular code design
* Handling edge cases and user input validation

## Description

Encodes or decodes messages using a simple Caesar Cipher. Version 2 adds:

* A **function** `caesar()` that handles encryption/decryption
* A **loop** that allows multiple messages without restarting the program
* A **logo** displayed at the start of the program
* **Input validation** for incorrect choices
* Maintains **non-alphabet characters** (numbers, symbols, spaces) unchanged

### Features

1. **Choose mode**: `encode` to encrypt, `decode` to decrypt
2. **Input message**: any string of text
3. **Shift number**: number of positions to shift letters
4. **Multiple runs**: choose to run the program again without restarting
5. **Supports lowercase letters** (currently), ignoring other characters

### Example output:

```
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world!
Type the shift number:
3
Here is the encoded result: khoor zruog!
```

```
Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
khoor zruog!
Type the shift number:
3
Here is the decoded result: hello world!
```

### Learning Goals

* Practice modular programming with functions
* Understand loops and control flow
* Learn basic encryption techniques with Caesar Cipher
* Handle input validation and edge cases
* Use modulo arithmetic for wrapping letters around the alphabet

## How to Run

```bash
python v2_caesar_cipher.py
```

> Make sure `v2_caesar_art.py` (with the `logo` variable) is in the same dir
