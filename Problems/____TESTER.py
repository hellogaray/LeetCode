import timeit

# Test arithmetic swap
arith_time = timeit.timeit("""
a = 123456
b = 789012
a = a + b
b = a - b
a = a - b
""", number=1000000)

# Test XOR swap
xor_time = timeit.timeit("""
a = 123456
b = 789012
a = a ^ b
b = a ^ b
a = a ^ b
""", number=1000000)

print(f"Arithmetic swap time: {arith_time}")
print(f"XOR swap time: {xor_time}")
