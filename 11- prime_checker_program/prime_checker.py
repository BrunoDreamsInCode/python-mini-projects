# Main function to check if a number is prime
def is_prime(num):
    raiz_num = int(num ** 0.5)  # Calculate the square root of the number

    # 0 and 1 are not prime numbers
    if num < 2:
        return False
    # 2 is the only even prime number
    if num == 2:
        return True
    # All other even numbers are not prime
    if num % 2 == 0:
        return False

    # Check for divisors from 3 to the square root of the number, only odd numbers
    for i in range(3, raiz_num + 1, 2):
        if num % i == 0:
            return False  # Found a divisor → not prime

    return True  # Any divisors found → prime number

# Example usage, it Will return True for prime, False if is not prime.
print(is_prime(73))