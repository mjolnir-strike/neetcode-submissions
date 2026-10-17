class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        hasZero = list()
        zeroCount = 0
        output = [0] * len(nums)
        for i in range(len(nums)):
            n = nums[i]
            if n != 0:
                product *= n
            else:
                hasZero.append(i)
                zeroCount += 1

        if zeroCount > 1:
            return output
    
        for i in range(len(nums)):
            n = nums[i]
            if zeroCount and n == 0:
                output[i] = product
            else:
                if zeroCount == 0:
                    output[i] = int(product / n)
        
        return output
