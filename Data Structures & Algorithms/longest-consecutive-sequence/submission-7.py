class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        # my_hash = {n: idx for idx, n in enumerate(nums)}

        
        for n in num_set:
            # Only check for the start of a sequence (i.e., n-1 doesn't exist)
            if (n - 1) not in num_set:
                length = 1
                while (n + length) in num_set:
                    length += 1
                longest = max(longest, length)
                
        return longest