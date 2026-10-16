class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
                return True
            else:
                counter[num] = 1
        
        return False
