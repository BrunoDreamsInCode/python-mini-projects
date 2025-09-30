Prime Number Checker
===================

> Simple Python exercise to check if a number is prime, inspired by beginner Python exercises (https://www.udemy.com/course/100-days-of-code/)

Python exercise focused on learning:

* Conditional statements (if, elif, else)
* Loops (for) and iteration
* Math operations and int() conversion
* Functions and modular code design
* Optimizing code using square root and skipping unnecessary checks
* Handling edge cases and input validation

Description
-----------

Checks whether a given number is a prime number. The program:

* Handles numbers less than 2 automatically (not prime)
* Recognizes 2 as the only even prime number
* Skips all other even numbers to optimize performance
* Checks only odd numbers up to the square root of the number
* Returns True if the number is prime, False otherwise

Features
--------

1. Input a number: any positive integer
2. Optimized prime check using square root
3. Ignores even numbers (except 2)
4. Function-based design (is_prime(num))
5. Clear return values: True or False
6. Example usage with print() for testing

Example output
--------------

print(is_prime(2))
## True

print(is_prime(4))
## False

print(is_prime(73))
## True

print(is_prime(100))
## False

Learning Goals
--------------

* Practice writing reusable functions
* Understand loops and control flow
* Learn basic optimization techniques for algorithms
* Handle edge cases correctly (0, 1, even numbers)
* Gain familiarity with mathematical operations in Python

How to Run
----------

python prime_checker.py

> Make sure your prime_checker.py contains the is_prime(num) function.
