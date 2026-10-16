from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # step 1 - frequency of each number in dict
        freq_dict = Counter(nums)
        
        # step 2 - create a bucket for frequency in index and the value as list of integer
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_dict.items():
            freq = freq_dict[num]
            bucket[freq].append(num)
            
        # step 3 - gather the top k from the buckets
        topK = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                topK.append(num)
                if len(topK) == k:
                    return topK
        return topK
    