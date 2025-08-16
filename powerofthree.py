class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # A power of 3 must be a positive integer (1, 3, 9, 27, ...)
        if n <= 0:
            return False

        # Keep dividing by 3 as long as n is divisible by 3
        # Example: 27 -> 9 -> 3 -> 1
        while n % 3 == 0:
            n //= 3   # integer division (no decimals)

        # If we reduced n all the way to 1, then n was a power of 3
