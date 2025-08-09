class Solution(object):
    def mySqrt(self, x):
        # Start with an initial guess for the square root
        guess = 1.0
        
        # Loop until the guess squared is close enough to x
        # abs() gets the absolute difference between guess^2 and x
        while abs(x - guess*guess) > 0.0001:
            # Update guess using Newton's method formula:
            # guess = guess - (f(guess) / f'(guess))
            # Here, f(guess) = guess^2 - x
            # derivative f'(guess) = 2 * guess
            guess = guess - (guess*guess - x) / (2 * guess)
        
        # Return the integer part of the guess as the sqrt approximation
        return int(guess)