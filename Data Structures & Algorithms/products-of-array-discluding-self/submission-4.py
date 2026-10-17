class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroCount = 0
        output = [0] * len(nums)
        for i in range(len(nums)):
            n = nums[i]
            if n != 0:
                product *= n
            else:
                zeroCount += 1

        if zeroCount > 1:
            return output
    
        for i in range(len(nums)):
            n = nums[i]
            if zeroCount == 1 and n == 0:
                output[i] = product
            else:
                if zeroCount == 0:
                    output[i] = int(product / n)
        
        return output
