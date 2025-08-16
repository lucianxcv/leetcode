class Solution:
    def maximum69Number(self, num: int) -> int:
        # Convert the number to a string, then to a list of characters
        # Example: 9669 -> "9669" -> ['9','6','6','9']
        s = list(str(num))

        # Loop through the list, with both index (i) and character (ch)
        for i, ch in enumerate(s):
            # If we find the first '6'...
            if ch == '6':
                # ...change it to '9'
                s[i] = '9'
                # Stop after the first replacement (leftmost '6' gives max value)
                break

        # Join the list back into a string -> "9969"
        # Convert it back to an integer -> 9969
        return int(''.join(s))
