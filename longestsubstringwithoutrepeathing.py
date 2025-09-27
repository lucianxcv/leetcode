class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}            # map character -> its most recent index
        start = 0                 # left boundary of current window (inclusive)
        max_len = 0               # best answer found so far

        for i, ch in enumerate(s):            # iterate over characters with their index
            # if ch was seen before and its last index is inside the current window,
            # move start right after that last occurrence to avoid duplicates
            if ch in last_seen and last_seen[ch] >= start:
                start = last_seen[ch] + 1

            last_seen[ch] = i                 # update the most recent index of ch
            # window length is from start to i (inclusive)
            current_len = i - start + 1
            if current_len > max_len:
                max_len = current_len        # update max if we found a longer one

        return max_len