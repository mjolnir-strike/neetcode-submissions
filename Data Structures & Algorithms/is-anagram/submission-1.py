class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        def char_count(n: str):
            char_counter = {}
            for char in n:
                if char in char_counter:
                    char_counter[char] += 1
                else:
                    char_counter[char] = 1
            return char_counter
        return char_count(s) == char_count(t)
