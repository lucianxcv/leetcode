class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Edge case: must be positive
        if n <= 0:
            return False

        # Keep dividing by 4 while possible
        while n % 4 == 0:
            n //= 4   # integer division

        # If in the end we got 1, it was a power of 4
        return n == 1
