# Function to calculate the sum of digits of a number
def sumOfDigits(n):
    # Initialize sum to 0
    sum = 0

    # Loop until n becomes 0
    while n != 0:
        # Add the last digit of n to sum (using modulus operator)
        sum += n % 10

        # Remove the last digit from n (using integer division)
        n //= 10

    # Return the final sum
    return sum


# Example usage
n = 12345
print("Sum of digits of", n, "is:", sumOfDigits(n))


# ------------------------
# Test cases for verification
# ------------------------
def test_sumOfDigits():
    assert sumOfDigits(12345) == 15  # 1+2+3+4+5 = 15
    assert sumOfDigits(0) == 0  # Sum of digits of 0 is 0
    assert sumOfDigits(9) == 9  # Single-digit number
    assert sumOfDigits(1001) == 2  # 1+0+0+1 = 2
    assert sumOfDigits(9999) == 36  # 9+9+9+9 = 36
    assert sumOfDigits(10) == 1  # 1+0 = 1
    print("All test cases passed!")


# Run the test cases
test_sumOfDigits()
