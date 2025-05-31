def is_prime(n):
    # A prime number is greater than 1
    if n <= 1:
        return False

    # Check for factors from 2 up to n - 1
    for i in range(2, n):
        # If n is divisible by any number between 2 and n-1, it's not prime
        if n % i == 0:  # <-- Corrected logic here
            return False

    # If no factors were found, n is prime
    return True

print(is_prime(-5))   # False, negative numbers are not prime
print(is_prime(0))    # False, 0 is not prime
print(is_prime(1))    # False, 1 is not prime
print(is_prime(2))    # True, 2 is the smallest prime number
print(is_prime(3))    # True, prime
print(is_prime(4))    # False, divisible by 2
print(is_prime(17))   # True, prime
print(is_prime(20))   # False, divisible by 2 and 5
