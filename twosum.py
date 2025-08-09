class Solution(object):
    def twoSum(self, nums, target):
        # Create a dictionary to store numbers we have seen so far and their indices
        previous_number = {}
        
        # Loop over each number and its index in the input list 'nums'
        for index, num in enumerate(nums):
            # Calculate the number needed to reach the target sum
            complement = target - num
            
            # Check if the complement number is already in the dictionary
            if complement in previous_number:
                # If found, return the pair of indices: index of complement and current index
                return (previous_number[complement], index)
            
            # If complement not found, add the current number and its index to the dictionary
            previous_number[num] = index