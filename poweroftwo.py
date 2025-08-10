def isPowerOfTwo(n: int) -> bool:
    # Function 'isPowerOfTwo' takes an integer 'n'
    # and returns True if 'n' is a power of 2, otherwise False.
    # The type hints (n: int -> bool) mean:
    #    n should be an int, and the function returns a bool.

    if n <= 0:
        # If n is zero or negative, it can't be a power of 2
        return False

    while n % 2 == 0:
        # While n is evenly divisible by 2 (no remainder)
        n //= 2
        # Divide n by 2 using integer division
        # Keep going until n is no longer divisible by 2

    return n == 1
    # If after repeatedly dividing by 2 we end up with 1,
    # then the original n was a power of 2.
    # Otherwise, it wasn't.

print(isPowerOfTwo(16))
print(isPowerOfTwo(3))
        

        