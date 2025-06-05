def reverse_digit(number):
    # Initialize the reversed number to 0
    reversed_number = 0

    # Continue until all digits are processed
    while number > 0:
        last_digit = number % 10                      # Extract the last digit
        reversed_number = reversed_number * 10 + last_digit  # Append to reversed number
        number = number // 10                         # Remove the last digit

    return reversed_number

# Testing Scenarios:

# Test Case 1: A normal positive number
print("Reverse of 12345:", reverse_digit(12345))

# Test Case 2: Single digit number
print("Reverse of 7:", reverse_digit(7))

# Test Case 3: Number ending with zero
print("Reverse of 1200:", reverse_digit(1200))

# Test Case 4: Zero
print("Reverse of 0:", reverse_digit(0))
