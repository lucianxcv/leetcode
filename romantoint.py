def romanToInt(s: str) -> int:
    # Step 1: Create a dictionary to map Roman symbols to their integer values
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    # Step 2: Initialize result variable
    total = 0

    # Step 3: Loop through each character in the string (by index)
    for i in range(len(s)):
        # Get the integer value of the current Roman numeral
        value = roman_map[s[i]]

        # Step 4: Look ahead to the next numeral (if it exists)
        if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
            # If the current value is smaller than the next one,
            # we subtract instead of adding (e.g. IV → 5 - 1 = 4)
            total -= value
        else:
            # Otherwise, we just add it normally
            total += value

    # Step 5: Return the final result
    return total