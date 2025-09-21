# Caesar Cipher Program

> Exercise from my current Python course. (https://www.udemy.com/course/100-days-of-code/)

Python exercise focused on learning:

- `input()` and user interaction  
- `for` loops and iteration  
- Conditional statements (`if`, `elif`, `else`)  
- Working with lists and `append()`  
- String manipulation using `"".join()`  

## Description

Encodes or decodes messages using a simple Caesar Cipher:

- Choose **encode** to encrypt or **decode** to decrypt a message  
- Enter the **message** you want to process  
- Enter the **shift number** (how many positions letters should move in the alphabet)  
- Program processes each letter and outputs the final message  
- Currently handles **lowercase letters only**; other characters are ignored  

### Example output:

```
Type 'encode' to encrypt and 'decode' to decrypt: encode
Type your message: hello
Type the shift number: 3
Results: khoor
```  

```
Type 'encode' to encrypt and 'decode' to decrypt: decode
Type your message: khoor
Type the shift number: 3
Results: hello
```

Each run with different messages or shift numbers produces a unique result based on the user input.

### Learning Goal

- Practice working with user input and control flow  
- Learn how to iterate over strings and manipulate lists  
- Understand basic encryption techniques using logic and modulo arithmetic  

## How to Run
```bash
python v1_cesar_cipher.py