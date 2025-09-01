class Solution:
    def isValid(self, s: str) -> bool:
        # Use a stack to keep track of opening brackets
        stack = []
        
        # Map closing brackets to their corresponding opening ones
        mapping = {')': '(', '}': '{', ']': '['}
        
        # Iterate through each character in the string
        for char in s:
            # If the character is a closing bracket
            if char in mapping:
                # Pop from stack if possible, else assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped element matches the correct opening bracket
                if mapping[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push onto stack
                stack.append(char)
        
        # If the stack is empty, all brackets were matched
        return not stack
