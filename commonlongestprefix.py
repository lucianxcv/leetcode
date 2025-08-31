class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # Edge case: if the list is empty, return empty string
        if not strs:
            return ""
        
        # Start by assuming the first string is the common prefix
        prefix = strs[0]
        
        # Compare the prefix with each string in the list
        for s in strs[1:]:
            # While the current string does not start with prefix
            while not s.startswith(prefix):
                # Shorten the prefix by removing the last character
                prefix = prefix[:-1]
                # If prefix becomes empty, there is no common prefix
                if not prefix:
                    return ""
        
        # After checking all strings, return the final prefix
        return prefix
